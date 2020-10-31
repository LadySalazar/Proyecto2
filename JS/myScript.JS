var totalProductos= new Array(100);
$("#Productos").hide();

$("#dropMenu").click(function(){
	$("#Productos").empty();
	$("#Productos").show();
	getProductos();
});

function getProductos(){
	console.log("entreee");
	$.ajax({
		url: "http://ec2-54-157-158-193.compute-1.amazonaws.com/cgi-bin/Proyecto2/controladorP.py",
		type: "GET",
		contentType: "application/json; charset=utf-8", 
		dataType:"JSON",

		success: function(respuesta){
			var con=0;
			var tabla="";
			con=0;
			var con2=0;
			var est=0;
			var t=0;
			var text5="";
			var text6="";
			var prueba="addd";
			for (var i = 0; i < respuesta.length; i++) {

				totalProductos[con]='<div class="card" id="card">'+
				'<img src="'+respuesta[i].imagen+'"></img>'+
				'<div class="content">'+
				'<div class="header">'+respuesta[i].nombre+'</div>'+
				'<div class="meta"><a>'+respuesta[i].TipoProducto+'</a></div>'+
				'<div class="description">'+respuesta[i].precio+'</div></div>'+
				' <div class="extra content"><button class="ui button">'+prueba+'</button></div></div>';
					$("#Productos").append(totalProductos[con]);
					console.log(totalProductos[con]);

					text5+='<li>'+'<a onclick="ponerNombreLabelActualizarProducto('+respuesta[i].idProducto+')" id="'+respuesta[i].idProducto+'" >'+respuesta[i].nombre+'</a>'+'</li>';
					text6+='<li>'+'<a onclick="ponerNombreLabelBorrarProducto('+respuesta[i].idProducto+')" id="'+respuesta[i].idProducto+'" >'+respuesta[i].nombre+'</a>'+'</li>';

					con++;
			}
			
		
		}

	});
}
