var $        = require("jquery");
var _        = require("underscore");
var Backbone = require("backbone");
Backbone.$ = $;

//Boton de menu de navegacion
var BotonUsuarioDato = require("../views/boton_usuario_dato");
var BotonCloseMenu = require("../views/boton_close_menu");
var BotonOpenMenu  = require("../views/boton_open_menu");

//Control de Asistencia
var PanelMenuEmpleado  = require("../views/empleados/panel_menu_empleado");
var InputHijo       = require("../views/empleados/input_hijo");
var InputHijoUpdate = require("../views/empleados/input_hijo_update");
var FotografiaLoad = require("../views/empleados/file_imagen_fotografia");
var FotografiaUpdateLoad = require("../views/empleados/file_imagen_fotografia_update");
var SelectInputDocumentoIdentificacionUpdate = require("../views/empleados/select_input_documento_identificacion_update");
var SelectInputDocumentoIdentificacion = require("../views/empleados/select_input_documento_identificacion");

var InputNumeroDocumentoIdentificacion = require("../views/empleados/input_numero_documento_identificacion");


var UsuariosView = require("../views/usuarios");
var Usuarios = require("../collections/usuarios");
var SearchBox = require("../views/search_box");


class Router extends Backbone.Router
{
    initialize () {
        this._bindRoutes();
        var boton_usuario_dato = new BotonUsuarioDato({el:$("#boton_usuario_dato_container")});
        var boton_open_menu = new BotonOpenMenu({el: $("#boton_open_menu_container")})
        var boton_close_menu = new BotonCloseMenu({el: $("#boton_close_menu_container")})
    }

    routes ()
    {
        return {
        	  ""                                         :"index",
            "empadronamiento-municipal/empadronados/"                         : "empadronados",
            "empadronamiento-municipal/empadronado/nuevo/"                     : "empadronado_nuevo",
            "empadronamiento-municipal/empadronado/:empadronado/modificar/"   : "empadronado_modificar",
        };
    }
    empadronados()
    {
        var search_empleado = new SearchBox({el:$("#container_search_registro") });
    }
    empadronado_nuevo()
    {
        var panel_menu_empleado = new PanelMenuEmpleado({el:$("#panel_menu")});
        var fotografia = new FotografiaLoad({el:$("#container_fotografia")});
        var select_input_documento_identificacion = new SelectInputDocumentoIdentificacion({el: $("#container_documento_identificacion")});
        var input_documento_identificacion = new InputNumeroDocumentoIdentificacion({el: $("#container_numero_documento_identificacion")});
    }
    empadronado_modificar(emapadronado)
    {
      var panel_menu_empleado = new PanelMenuEmpleado({el:$("#panel_menu")});
      var fotografia = new FotografiaLoad({el:$("#container_fotografia")});
      var select_input_documento_identificacion = new SelectInputDocumentoIdentificacion({el: $("#container_documento_identificacion")});
      var input_documento_identificacion = new InputNumeroDocumentoIdentificacion({el: $("#container_numero_documento_identificacion")});
    }
}

module.exports = Router;
