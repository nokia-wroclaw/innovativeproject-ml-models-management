export const fetchWrapper = async (request:Request):Promise<Response> =>{
	return fetch(request);
}