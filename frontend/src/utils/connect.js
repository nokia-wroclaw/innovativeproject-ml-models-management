import {CredsStore} from "../user/CredsStore";
import {post,get} from "./fetch"
import {build as buildGetQuerry} from "./getParameters"

export const Auth = {
	login: async (username, password, reamember) => {
		const resp = await post(`auth/login/`,{
			"login":username,
			"password":password
		})
		if(resp.successful) {
			CredsStore.update(true,resp.data);
			const nextQueryTimeout = resp.data.valid_for * 2/3 * 1000;
			setTimeout( Auth.refresh, nextQueryTimeout )
		}
		else{
			CredsStore.update(false,null)
		}
		return resp;
	},
	refresh: async () => {
		const resp = await get(`auth/token/`)
		if(resp.successful) {
			CredsStore.update(true,resp.data);
			const nextQueryTimeout = resp.data.valid_for * 2/3 * 1000;
			setTimeout( Auth.refresh, nextQueryTimeout )
		}
		else{
			CredsStore.update(false,null)
		}
	}
}

export const User = {
	register: async ({email, password, name}) => {
		const resp = await post(`auth/login/`,{
			"login":email,
			"password":password,
			"name":name
		})
		if(resp.successful) {
			CredsStore.update(true,resp.data);
			const nextQueryTimeout = resp.data.valid_for * 2/3 * 1000;
			setTimeout( Auth.refresh, nextQueryTimeout )
		}
		else{
			CredsStore.update(false,null)
		}
		return resp;
	},
	getUser: async (userId) => {
		return await get(`users/${userId}/`);
	},
	getUsers: async () => {
		return await get("users/");
	},
	getUserModels: async (userId) => {
		return await get(`models/?user=${userId}`)
	}
}

export const Project = {
	getProject: async (projectId) => {
		return await get(`projects/${projectId}/`);
	},
	getProjects: async () => { 
		return await get("projects/");
	}
}

export const Model = {
	getModel: async (modelId) => {
		return await get(`models/${modelId}/`)
	},
	getModels: async (querry,projectId) => {
		const args = [{id:"query",val:querry}];
		if(projectId) args.push({id:"project",val:projectId})
		let query = 'models/' + buildGetQuerry(args)
		return await get(query);
	}
}