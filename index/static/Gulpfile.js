var gulp 	   			= require('gulp');
var gulp_uglify	    	= require('gulp-uglify');
var gulp_modernizr 		= require('gulp-modernizr');

var browserify      	= require('browserify');
var babelify   			= require('babelify');
var buffer     			= require('vinyl-buffer');
var source     			= require('vinyl-source-stream');

gulp.task('es6Toes5', function () {
	var jsSrc = "./javascriptdev/main.js";
	var jsDst = "./javascript/";
 	return browserify({
					    entries: (jsSrc),
					    debug: true
					  }).transform("babelify", { presets: ["es2015"], sourceMapsAbsolute: true})
 						.bundle()
 						
					    .pipe(source('main.js'))
					    .pipe(buffer())
					    .pipe(gulp_uglify())
					    .pipe(gulp.dest(jsDst));
});

gulp.task('watch', function(){
  gulp.watch('./app/javascript/backbone/main.js', ['es6Toes5']);
});


gulp.task('default', ['watch']);