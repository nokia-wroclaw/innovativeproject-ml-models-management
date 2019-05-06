// export interface Response {
// 	successful: boolean;
// 	errorCode?: string;
// 	errorDescription?: string;
// }
// export interface LoginResponse extends Response {
// 	jwt?: string;
//
// }
import {CredsStore} from "../store/CredsStore";
import {post,get} from "./fetch"
import {apiHost} from "./networkConfig";

export const Auth = {
	login: async (username, password, reamember) => {
		const resp = await post("auth/login/",{
			"login":username,
			"password":password
		})
		if(resp.text==="OK") CredsStore.setToken(resp.payload.access_token);
		console.log(resp)
		return {
			successful: resp.text === "OK",
			jwt: resp.payload.access_token
		}
	},
	register: async (firstname, lastname, email, password) => {
		return {
			successful: false,
			errorCode: "not-implemented",
			errorDescription: "register has not been implemented"
		}
	},
	recover: async (email) => {
		return {
			successful: false,
			errorCode: "not-implemented",
			errorDescription: "recover has not been implemented"
		}
	}
}
// export interface Parameter {
// 	id: string;
// 	value: number | string;
// }
// export interface Metric {
// 	id: string;
// 	value: number;
// }
// export interface Author{
// 	nick:string;
// 	name:string;
// 	url:string;
// }
// export interface Model {
// 	id: number;
// 	name: string;
// 	description: string;

// 	dataset: string;
// 	commitUrl: string;

// 	parameters: Parameter[];
// 	hyperParameters: Parameter[];
// 	metrics: Metric[];
// 	tags: string[];

// 	author: Author;
// }
// export interface Project {
// 	id: number;
// 	name: string;
// 	description: string;
// }
// export interface ProjectDetails extends Project {
// 	repoUrl: string;
// 	allParameters: string[];
// 	allHyperParameters: string[];
// 	allModelNames: string[];
// 	allModelTags: string[];
// 	allMetrics: string[];
// }
// export interface GetProjectResponse extends Response, ProjectDetails {
// }
// export interface GetProjectsResponse extends Response {
// 	projects?: Project[];
// }
export const Project = {
	// getProject: async (projectId) => {
	// 	return {
	// 		successful: true,
	// 		id: 2,
	// 		name: "Dystopian Face Recognition",
	// 		description: "For Continental China ONLY",
	// 		repoUrl: "--",
	// 		allParameters: ["cert","riskFactor","psychopassImportance"],
	// 		allHyperParameters: ["whitesHatered","racismFactor"],
	// 		allModelNames: ["riskAprox","colorAssign","policePreamptiveDispatcher"],
	// 		allModelTags: ["deployed","wasteful","notEnoughHard","toSoft","BIASED"],
	// 		allMetrics: ["acc","falsePositives","falseNegatives","missedWhites"],
	// 		allBranches: ["master","master-dev","deplyed"]
	// 	}
	// },
	getProject: async (projectId) => {
		const resp = await get('projects/'+projectId+'/');
		console.dir(resp)
		if(resp.text==="OK") return {
			successful: resp.text === "OK",
			id: resp.payload.id,
			name: resp.payload.name,
			description: resp.payload.description,
			repoUrl: resp.payload.git_url,
			commitUrl: resp.payload.git_,
			allParameters: resp.payload.all_parameters,
			allHyperParameters: resp.payload.all_hyperparameters,
			allMetrics: resp.payload.all_metrics,
			allModelTags: ["version:1.0.0", "scikit-learn"],
			allBranches: ["master", "master-dev", "develop"]
		}
		return {
			successful:false
		}
	},
	getProjects: async () => {
		return {
			successful: true,
			projects:[
				{
					id: 1,
					name: "string",
					description: "string",
				}
			]
		}
	}
}
// export interface GetModelResponse extends Response, Model {
// }
// export interface GetModelsResponse extends Response {
// 	models?: Model[];
// }
// export interface GetModelsQuery {
// 	filter?:{
// 		projectId:string,
// 		tags:string[],
// 		name:string,
// 		hyperParameters:string[],
// 		parameters:string[],
// 		metrics:string,
// 	},
// 	sort?:{
// 		order:"asc"|"desc",
// 		type:"field"|"metric"|"parameter"|"hyperParameter",
// 		id:string|number,
// 	},
// 	pagination?:{
// 		pageSize:number;
// 		startWithId?:number; // by default don't skip any
// 	}
// }
export const Model = {
	getModel: async (modelId) => {
		return {
			successful: true,
			id: 1,
			name: "string",
			description: "string",
			dataset: "string",
			commitUrl: "string",
			parameters: [{ id: "11", value: 22 }],
			hyperParameters: [{ id: "11", value: 22 }],
			metrics: [{ id: "11", value: 22 }],
			tags: ["tag","ojej","deployed","faulty","BIASED"],
			author:{
				name:"name",
				nick:"nick",
				url:"url.example.com/author/17"
			}
		}
	},
	getModels: async (projectId) => {
		const resp = await get('models/?projects='+projectId);
		console.info(resp)
		if(resp.text==="OK") return {
			successful: resp.text==="OK",
			models: resp.payload.map(rem => (
				{
					id: rem.id,
					name: rem.name,
					description: "decription of the model shall be here",
					dataset: rem.dataset.name,
					commitUrl: "string",
					parameters: rem.parameters,
					hyperParameters: rem.hyperparameters,
					metrics: rem.metrics,
					tags: ["tag","ojej","deployed","faulty"],
					author:{
						name:rem.user.full_name,
						nick:rem.user.login,
						url:""
					}
				}
			))
		}
		return {
			successful:false
		}
	}
}