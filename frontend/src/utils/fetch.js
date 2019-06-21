import {CredsStore} from "../user/CredsStore";
import {apiHost} from "./networkConfig";

export const attachToken = (req)=>{
	if(CredsStore.getCreds() && CredsStore.getCreds().access_token){
		req.headers.set('Accept', '*/*') // for dev only
		req.headers.set('Authorization', 'Bearer ' + CredsStore.getCreds().access_token)
	}
	return req;
}
export const send = async (req)=>{
	attachToken(req);
	return extract(fetch(req));
}
export const get = async (uri)=>{
 	const req = new Request(apiHost+uri);
	attachToken(req);
	return extract(fetch(req));
}
export const post = async (uri,payload)=>{
	if(typeof payload !== "string") payload = JSON.stringify(payload);
	const req = new Request(apiHost+uri, {method: 'POST', body: payload});
	attachToken(req);
	req.headers.set('Content-Type', 'application/json')
	return extract(fetch(req));
}
export const extract = async (response)=>{
	const resp = await response;
	let payload = await resp.json();
	if(typeof payload === "undefined") payload = {};
	payload.responseStatus = resp.status;
	payload.text = resp.statusText;
	payload.successful = resp.statusText === "OK";
	return payload;
}