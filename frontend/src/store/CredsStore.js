class CredsStoreClass{
	notify = new Map();
	getToken = () => localStorage.getItem("token");
	setToken = (newToken) => {
		localStorage.setItem("token",newToken)
		Array.from(this.notify.values()).forEach(handler => handler(newToken))
	}
	subscribeToken = (id,handler) => {
		this.notify.set(id,handler);
		return localStorage.getItem("token");
	}
	unSubscribeToken = (id) => this.notify.delete(id);
}
export const CredsStore = new CredsStoreClass();
window.CredsStore = CredsStore;