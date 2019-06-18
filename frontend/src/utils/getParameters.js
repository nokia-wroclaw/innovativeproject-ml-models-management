/* expect array of objects implementing interface 
{
	id:"";
	val:"";
}
*/

function buildArg(arg){
	if(arg.val) return `${arg.id}=${arg.val}`;
	return `${arg.id}`
}

export function build(arr){
	if(arr.length === 0) return "";
	return `?${arr.map(buildArg).join("&")}`;
}