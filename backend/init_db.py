import uuid
import string

from random import randint, shuffle, sample, choice

from app.models import User, Project, Workspace, Model
from app import db


DESCRIPTION = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Quisque rhoncus, enim id imperdiet aliquam, purus augue aliquam justo, "
    "nec efficitur lorem massa a orci. "
    "Sed semper enim turpis, sed pellentesque sapien condimentum et. "
    "Donec sed urna aliquam, ornare lorem sollicitudin, rhoncus eros. "
    "Sed sollicitudin urna ac lectus tincidunt, ut pretium lorem congue. "
    "Integer ac convallis ipsum. "
    "Cras mollis odio id leo lobortis tristique. "
    "Curabitur varius faucibus diam a commodo. "
    "Suspendisse dapibus nisi ut tempus tempor. "
    "Nunc egestas sapien ac semper mollis."
)

NOUNS = (
    "floor sign ship ladybug cattle weather drop badge purpose week honey "
    "ground stone school apparatus cat death cent transport farm pig effect "
    "maid hydrant month tank pail record approval hair watch horse voice "
    "harmony protest wish quill title rice attraction club pie lumber "
    "substance trees grass volleyball door cats bedroom thread mountain "
    "milk distribution board way sun adjustment engine pets yak coach route "
    "shame tent monkey head debt end waves leather top hat hammer offer cellar "
    "bomb knee rub time sand smell wrist stem library branch toy education "
    "front jellyfish night comparison low curtain rain pies nest train mist level"
).split(" ")

ADJECTIVES = (
    "deadpan mountainous flowery victorious brave alive enthusiastic rightful "
    "cultured large busy careless materialistic hot greedy spicy organic "
    "heartbreaking disagreeable pushy lumpy gaudy wrong worthless knowledgeable "
    "long berserk telling ahead neat lying spiky efficacious cut confused "
    "staking delicate whimsical hideous flimsy quizzical erect envious sedate "
    "combative curious overjoyed terrific even flippant understood round "
    "direful luxuriant unique cuddly lamentable tight heavy tangible slow "
    "lively scintillating purple nine successful majestic adjoining scattered "
    "futuristic unruly hesitant fat nervous sable makeshift parched future "
    "actually deranged powerful wakeful ill-fated violent jagged tense purring "
    "fine fast short nimble protective quaint tranquil scandalous aspiring "
    "obsequious stingy hard soft"
).split(" ")


def add_default_user(
    login: str = "admin",
    password: str = "admin",
    full_name: str = "Maisie Admin Account",
    email: str = "admin@maisie.dev",
) -> int:
    user = User.query.filter_by(login=login).first()
    if not user:
        user = User(login=login, full_name=full_name, password=password, email=email)
        db.session.add(user)
        if db.session.commit():
            print("Added user:", user)
    else:
        print(f"User `{login}` already exists, skipping.")

    return user.id


def add_default_workspace(user_id: int = 1, name: str = "Default workspace") -> int:
    workspace = Workspace.query.first()
    if not workspace:
        workspace = Workspace(name=name, description=DESCRIPTION)
        db.session.add(workspace)
        if db.session.commit():
            print("Added workspace:", workspace)
    else:
        print("Default workspace already exists, reusing")

    return workspace.id


def add_default_project(workspace_id: int = 1, name: str = "Default project") -> int:
    project = Project(
        name=name,
        description=DESCRIPTION,
        workspace_id=workspace_id,
        git_url="https://github.com/nokia-wroclaw/innovativeproject-ml-models-management",
    )
    db.session.add(project)
    if db.session.commit():
        print("Added project:", project)

    return project.id


def get_random_dictionary(low: int = 10, high: int = 20):
    letters = list(string.ascii_lowercase)
    full_letters = [
        "".join([letter, str(number)])
        for letter in letters
        for number in range(1, high)
    ]

    elements_count = randint(low, high)
    shuffle(full_letters)
    keys = full_letters[0:elements_count]
    values = sample(range(0, 500), elements_count)
    values = map(lambda x: x / 500, values)

    return dict(zip(keys, values))


def get_random_name(
    words: int = 2, separator: str = "", capitalize: bool = True
) -> str:
    result = [choice(NOUNS)]
    if words > 0:
        for i in range(words - 1):
            result.append(choice(ADJECTIVES))

    if capitalize:
        result = list(map(lambda x: str(x).capitalize(), result))

    return separator.join(result[::-1])


def get_random_hash(length: int = 40) -> str:
    return "".join(choice(string.ascii_letters + string.digits) for _ in range(length))


def add_random_models(
    user_id: int = None, project_id: int = None, count: int = 25
) -> None:
    users = User.query.all()
    projects = Project.query.all()
    for i in range(count):
        name = get_random_name(separator=" ")
        number = randint(10, 50)

        # if given, assign the user
        selected_user_id = choice(users).id
        if user_id != None:
            selected_user_id = user_id

        selected_project_id = choice(projects).id
        # if given, assign the project
        if project_id != None:
            selected_project_id = project_id

        print(
            f"#{i+1} Adding model `{name}` to project_id {selected_project_id} with user_id {selected_user_id}"
        )

        hyperparameters = get_random_dictionary(10, 20)
        parameters = get_random_dictionary(10, 100)
        metrics = get_random_dictionary(5, 15)

        new_model = Model(
            user_id=selected_user_id,
            project_id=selected_project_id,
            hyperparameters=hyperparameters,
            parameters=parameters,
            metrics=metrics,
            name=f"Randomized: {name}",
            path=uuid.uuid4(),
            dataset_name=f"Random dataset #{number}",
            dataset_description=DESCRIPTION,
            git_active_branch="develop",
            git_commit_hash="29ea5f511668248ea7ffe229c0f09992aaa6b382",
            private=False,
        )
        db.session.add(new_model)
    db.session.commit()


def add_random_users(password: str = "pass", count: int = 20) -> None:
    for i in range(count):
        login = "demo" * 6
        while len(login) > 20:
            full_name = get_random_name(separator=" ")
            login = full_name.replace(" ", "_").lower() + str(randint(10, 500))
        print(f"#{i+1} Adding user `{login}`")

        add_default_user(
            login=login,
            password="pass",
            full_name=full_name,
            email=f"random_{get_random_hash(30)}@maisie.dev",
        )


def add_random_projects(count: int = 20, user_id: int = None) -> None:
    # users = User.query.all()
    for i in range(count):
        # if not given, select a random user
        # if user_id == None:
        # user_id = choice(users).id

        name = get_random_name(separator=" ")
        name = name + " " + str(randint(10, 500))
        print(f"#{i+1} Adding project `{name}`")
        add_default_project(name=name)


def run_all(
    user_login: str = "Nokia2019",
    user_password: str = "DemoNokia2019",
    models_count: int = 10,
) -> None:
    user_id = add_default_user(login=user_login, password=user_password)
    workspace_id = add_default_workspace(user_id)
    project_id = add_default_project(workspace_id)

    add_random_models(user_id=user_id, project_id=project_id, count=models_count)


def run_all_random(
    models_count: int = 200, users_count: int = 10, projects_count: int = 5
) -> None:
    add_random_users(count=users_count)
    add_random_projects(count=projects_count)
    add_random_models(count=models_count)
