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