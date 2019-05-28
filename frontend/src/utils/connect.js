import {CredsStore} from "../store/CredsStore";
import {post,get} from "./fetch"
import {apiHost} from "./networkConfig";
import {build as buildGetQuerry} from "./getParameters"

export const Auth = {
	login: async (username, password, reamember) => {
		const resp = await post(`auth/login/`,{
			"login":username,
			"password":password
		})
		if(resp.successful) {
			CredsStore.setCreds(resp.data);
			const nextQueryTimeout = resp.data.valid_for * 2/3 * 1000;
			setTimeout( Auth.refresh, nextQueryTimeout )
		}
		return resp;
	},
	refresh: async () => {
		const resp = await get(`auth/token/`)
		if(resp.successful) {
			CredsStore.setCreds(resp.data);
			const nextQueryTimeout = resp.data.valid_for * 2/3 * 1000;
			setTimeout( Auth.refresh, nextQueryTimeout )
		}
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

export const User = {
	getProject: async (userId) => {
		return await get(`users/${userId}/`);
	},
	getProjects: async () => {
		return await get("users/");
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