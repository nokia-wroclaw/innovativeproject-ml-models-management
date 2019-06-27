/*
	"token": "wtgiwghg420gh04hg0234hg0gi35hgi35hgi53g55h46hjn="
	"id": 1,
	"login": "Clechay",
	"full_name": "Łukasz Kleczaj",
	"email": "admin@maisie.dev"
*/ 


class CredsStoreClass{
	constructor(){
		this.state = {
			loggedIn: false,
			creds: this._loadCreds() || {}
		}
		this.notify = new Map();
	}

	_saveCreds = (obj) => {
		this.state.creds = obj;
		localStorage.setItem("creds",JSON.stringify(obj));
	}
	_loadCreds = () => {
		return JSON.parse(localStorage.getItem("creds"));
	}
	
	_emmit = () => {
		const creds = this.getCreds();
		Array.from(this.notify.values()).forEach(handler => handler(this.state));
	}
	
	getState = () => {
		return this.state;
	}
	getCreds = () => {
		return this.state.creds;
	}
	getLoggedIn = () => {
		return this.state.loggedIn;
	}
	update(loggedIn,newCreds){
		this.state.loggedIn = loggedIn;
		this._saveCreds(newCreds);
		this._emmit();
	}

	subscribe = (id,handler) => {
		this.notify.set(id,handler);
		return this.getCreds();
	}
	subscribeLoggedIn = (id,handler) => {
		this.notify.set(id,(state)=>handler(state.loggedIn));
		return this.getCreds();
	}
	subscribeCreds = (id,handler) => {
		this.notify.set(id,(state)=>handler(state.creds));
		return this.getCreds();
	}
	unSubscribe = (id) => this.notify.delete(id);
}
export const CredsStore = new CredsStoreClass();
window.CredsStore = CredsStore;