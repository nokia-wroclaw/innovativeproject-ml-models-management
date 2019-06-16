import { decorate, observable } from 'mobx';

class AccountStore {
	 @observable loggedIn = false;
	 @observable nick = "";
}

export const store = new AccountStore;
export default store;