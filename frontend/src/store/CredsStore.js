/*
token:""
nick:""
*/ 


function saveCreds(obj){
	localStorage.setItem("creds",JSON.stringify(obj))
}


class CredsStoreClass{
	notify = new Map();
	emmit = () => {
		// const creds = this.getCreds();
		// Array.from(this.notify.values()).forEach(handler => handler(creds));
	}
	getCreds = () => {
		const creds = localStorage.getItem("creds");
		return JSON.parse(creds);
	}
	setCreds = (newCreds) => {
		saveCreds(newCreds);
		this.emmit();
	}
	updateCreds = (path) => {
		const newCreds = this.getCreds();
		for (const key in path) {
			newCreds[key] = path[key];
		}
		saveCreds(newCreds);
		this.emmit();
	}
	subscribeToken = (id,handler) => {
		this.notify.set(id,handler);
		return this.getCreds();
	}
	unSubscribeToken = (id) => this.notify.delete(id);
}
export const CredsStore = new CredsStoreClass();
window.CredsStore = CredsStore;