import {CredsStore} from "../store/CredsStore";
import {post,get} from "./fetch"
import {apiHost} from "./networkConfig";

export const Auth = {
	login: async (username, password, reamember) => {
		const resp = await post(`auth/login/`,{
			"login":username,
			"password":password
		})
		if(resp.successful) {
			CredsStore.setToken(resp.data.access_token);
			const nextQueryTimeout = resp.data.valid_for * 2/3 * 1000;
			// console.log(`seting timeout for ${nextQueryTimeout}`,resp)
			setTimeout( Auth.refresh, nextQueryTimeout )
		}
		return resp;
	},
	refresh: async () => {
		const resp = await get(`auth/token/`)
		if(resp.successful) {
			CredsStore.setToken(resp.data.access_token);
			const nextQueryTimeout = resp.data.valid_for * 2/3 * 1000;
			// console.log(`seting timeout for ${nextQueryTimeout}`,resp)
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

export const Model = {
	getModel: async (modelId) => {
		return await get(`models/${modelId}/`)
	},
	getModels: async (meta) => {
		let query = 'models/?project='+meta.project+'&';
		if(meta.parameters&&meta.parameters.length) query+="parameters="+meta.parameters.join(",")+"&";
		if(meta.hyperparameters&&meta.hyperparameters.length) query+="hyperparameters="+meta.hyperparameters.join(",")+"&";
		if(meta.metrics&&meta.metrics.length) query+="metrics="+meta.metrics.join(",")+"&";
		if(query.endsWith("&")) query = query.slice(0,-1);
		return await get(query);
	}
}