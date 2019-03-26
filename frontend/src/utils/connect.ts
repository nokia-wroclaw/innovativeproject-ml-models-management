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
	register: async (firstname: string, lastname:string, email:string, password: string): Promise<Response> => {
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
interface Parameter{
	id:string;
	value:number;
}
interface Model{
	parameters?:Parameter[];
	hiperParameters?:Parameter[];
	dataset?:string;
	commitUrl?:string;
}
interface Project{
	id?:string;
	name?:string;
}
interface ProjectDetails extends Project{
	repoUrl?:string;
	allParameters?:string[];
	allHiperParameters?:string[];
}
interface GetProjectResponse extends Response, ProjectDetails{
}
interface GetProjectsResponse extends Response {
	projects?:Project[];
}
export const Project = {
	getProject: async (projectId:string): Promise<GetProjectResponse> => {
		return {
			successful: false,
			errorCode: "not-implemented",
			errorDescription: "getProject has not been implemented"
		}
	},
	getProjects: async (): Promise<GetProjectsResponse> => {
		return {
			successful: false,
			errorCode: "not-implemented",
			errorDescription: "getProjects has not been implemented"
		}
	}
}
interface GetModelResponse extends Response, Model{
}
interface GetModelsResponse extends Response {
	Models?:Model[];
}
export const Model = {
	getModel: async (modelId:string): Promise<GetModelResponse> => {
		return {
			successful: false,
			errorCode: "not-implemented",
			errorDescription: "getModel has not been implemented"
		}
	},
	getModels: async (projectId:string): Promise<GetModelsResponse> => {
		return {
			successful: false,
			errorCode: "not-implemented",
			errorDescription: "getModels has not been implemented"
		}
	}
}