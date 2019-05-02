// export interface Response {
// 	successful: boolean;
// 	errorCode?: string;
// 	errorDescription?: string;
// }
// export interface LoginResponse extends Response {
// 	jwt?: string;
// }
export const Auth = {
	login: async (username, password, reamember) => {
		return {
			successful: false,
			errorCode: "not-implemented",
			errorDescription: "log-in has not been implemented"
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
// 	hiperParameters: Parameter[];
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
// 	allHiperParameters: string[];
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
	getProject: async (projectId) => {
		return {
			successful: true,
			id: 1,
			name: "Dystopian Face Recognition",
			description: "For Continental China ONLY",
			repoUrl: "--",
			allParameters: ["cert","riskFactor","psychopassImportance"],
			allHiperParameters: ["whitesHatered","racismFactor"],
			allModelNames: ["riskAprox","colorAssign","policePreamptiveDispatcher"],
			allModelTags: ["deployed","wasteful","notEnoughHard","toSoft","BIASED"],
			allMetrics: ["acc","falsePositives","falseNegatives","missedWhites"],
			allBranches: ["master","master-dev","deplyed"]
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
// 		hiperParameters:string[],
// 		parameters:string[],
// 		metrics:string,
// 	},
// 	sort?:{
// 		order:"asc"|"desc",
// 		type:"field"|"metric"|"parameter"|"hiperParameter",
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
			hiperParameters: [{ id: "11", value: 22 }],
			metrics: [{ id: "11", value: 22 }],
			tags: ["tag","ojej","deployed","faulty","BIASED"],
			author:{
				name:"name",
				nick:"nick",
				url:"url.example.com/aurhor/17"
			}
		}
	},
	getModels: async (projectId) => {
		return {
			successful: true,
			models: [
				{
					id: 1,
					name: "string",
					description: "string",
					dataset: "string",
					commitUrl: "string",
					parameters: [{ id: "11", value: 22 }],
					hiperParameters: [{ id: "11", value: 22 }],
					metrics: [{ id: "11", value: 22 }],
					tags: ["tag","ojej","deployed","faulty","BIASED"],
					author:{
						name:"name",
						nick:"nick",
						url:"url.example.com/aurhor/17"
					}
				},
				{
					id: 1,
					name: "string",
					description: "string",
					dataset: "string",
					commitUrl: "string",
					parameters: [{ id: "11", value: 22 }],
					hiperParameters: [{ id: "11", value: 22 }],
					metrics: [{ id: "11", value: 22 }],
					tags: ["tag","ojej","deployed","faulty","BIASED"],
					author:{
						name:"name",
						nick:"nick",
						url:"url.example.com/aurhor/17"
					}
				},
				{
					id: 1,
					name: "string",
					description: "string",
					dataset: "string",
					commitUrl: "string",
					parameters: [{ id: "11", value: 22 }],
					hiperParameters: [{ id: "11", value: 22 }],
					metrics: [{ id: "11", value: 22 }],
					tags: ["tag","ojej","deployed","faulty","BIASED"],
					author:{
						name:"name",
						nick:"nick",
						url:"url.example.com/aurhor/17"
					}
				},
				{
					id: 1,
					name: "string",
					description: "string",
					dataset: "string",
					commitUrl: "string",
					parameters: [{ id: "11", value: 22 }],
					hiperParameters: [{ id: "11", value: 22 }],
					metrics: [{ id: "11", value: 22 }],
					tags: ["tag","ojej","deployed","faulty","BIASED"],
					author:{
						name:"name",
						nick:"nick",
						url:"url.example.com/aurhor/17"
					}
				}
			]
		}
	}
}