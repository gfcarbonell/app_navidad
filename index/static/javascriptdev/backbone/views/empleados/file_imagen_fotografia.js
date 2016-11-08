var $           = require("jquery");
var _           = require("underscore");
var Backbone 	= require("backbone");
Backbone.$ = $;


class FileImagen extends Backbone.View
{

	initialize()
	{
		this.template = _.template($("#imagen_template").html());
		this.render();
	}
	events()
	{
		return {
				"change #id_fotografia"  			  : "load_imagen",
		};
	}

	load_imagen(e)
	{
		var file = e.target.files[0];
    var imageType = /image.*/;

    if (!file.type.match(imageType))
      return;
    var reader = new FileReader();
    reader.onload = this.fileOnload;
    reader.readAsDataURL(file);
	}
  fileOnload(e) {
    var result=e.target.result;
    $("#panel_left_imagen").attr("src",result);
  }

  render()
	{
      this.$el.html(this.template());
		  return this;
  }

}

module.exports = FileImagen;
