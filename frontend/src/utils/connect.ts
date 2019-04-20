export interface Response {
	successful: boolean;
	errorCode?: string;
	errorDescription?: string;
}
export interface LoginResponse extends Response {
	jwt?: string;
}
export const Auth = {
	login: async (username: string, password: string, reamember: boolean): Promise<LoginResponse> => {
		return {
			successful: false,
			errorCode: "not-implemented",
			errorDescription: "log-in has not been implemented"
		}
	},
	register: async (firstname: string, lastname: string, email: string, password: string): Promise<Response> => {
		return {
			successful: false,
			errorCode: "not-implemented",
			errorDescription: "register has not been implemented"
		}
	},
	recover: async (email: string): Promise<Response> => {
		return {
			successful: false,
			errorCode: "not-implemented",
			errorDescription: "recover has not been implemented"
		}
	}
}
export interface Parameter {
	id: string;
	value: number | string;
}
export interface Metric {
	id: string;
	value: number;
}
export interface Author{
	nick:string;
	name:string;
	url:string;
}
export interface Model {
	id: number;
	name: string;
	description: string;

	dataset: string;
	commitUrl: string;

	parameters: Parameter[];
	hiperParameters: Parameter[];
	metrics: Metric[];
	tags: string[];

	author: Author;
}
export interface Project {
	id: number;
	name: string;
	description: string;
}
export interface ProjectDetails extends Project {
	repoUrl: string;
	allParameters: string[];
	allHiperParameters: string[];
	allModelNames: string[];
	allModelTags: string[];
	allMetrics: string[];
}
export interface GetProjectResponse extends Response, ProjectDetails {
}
export interface GetProjectsResponse extends Response {
	projects?: Project[];
}
export const Project = {
	getProject: async (projectId: number): Promise<GetProjectResponse> => {
		return {
			successful: true,
			id: 1,
			name: "string",
			description: "string",
			repoUrl: "string",
			allParameters: ["string"],
			allHiperParameters: ["string"],
			allModelNames: ["name"],
			allModelTags: ["tag","ojej","deployed","faulty","BIASED"],
			allMetrics: ["acc"]
		}
	},
	getProjects: async (): Promise<GetProjectsResponse> => {
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
export interface GetModelResponse extends Response, Model {
}
export interface GetModelsResponse extends Response {
	models?: Model[];
}
export interface GetModelsQuery {
	filter?:{
		projectId:string,
		tags:string[],
		name:string,
		hiperParameters:string[],
		parameters:string[],
		metrics:string,
	},
	sort?:{
		order:"asc"|"desc",
		type:"field"|"metric"|"parameter"|"hiperParameter",
		id:string|number,
	},
	pagination?:{
		pageSize:number;
		startWithId?:number; // by default don't skip any
	}
}
export const Model = {
	getModel: async (modelId: string): Promise<GetModelResponse> => {
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
	getModels: async (projectId: number): Promise<GetModelsResponse> => {
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
				}
			]
		}
	}
}