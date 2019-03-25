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