import React from 'react';

export const Row = (props) => {
	return <div style={{display:"flex",flexDirection:"row"}}>
		{props.children || ""}
	</div>;
}
export const Col = (props) => {
	return <div style={{display:"flex",flexDirection:"column"}}>
		{props.children || ""}
	</div>;
}
export const CenterBox = (props) => {
	return <div style={{
		width:"100%",
		height:"100%",
		display:"flex",
		flexDirection:"column",
		justifyContent:"center",
		alignItems:"center"}}>

		{props.children || ""}
	</div>;
}