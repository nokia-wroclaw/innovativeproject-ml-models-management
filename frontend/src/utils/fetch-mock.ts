import {apiHost} from './networkConfig';

const model = {
	id : 11,
	user_id : 22,
	project_id : 44,
	hyperparameters : {a:"b"},
	parameters : {c:"d"},
	name : "abc",
	path : "",
	// dataset_name : db.Column(db.String(120), default:None),
	// dataset_description : db.Column(db.Text, default:None),
	// private : db.Column(db.Boolean, default:False),
	// updated : db.Column(db.DateTime, nullable:False, default:datetime.utcnow),
	// created : db.Column(db.DateTime, nullable:False, default:datetime.utcnow),
}

// const urls:[RegExp,any][] = []
// urls.push(
// 	[RegExp(apiHost+'model/\w+'),]
// )


// export const fetchWrapper = async (request: Request): Promise<Response> => {
		
// 	return new Response(undefined, { status: 404 });
// }