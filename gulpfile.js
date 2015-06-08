var gulp = require('gulp'),
    less = require('gulp-less'),
    path = require('path'),
    watch = require('gulp-watch');

gulp.task('default', function () {
  return gulp.src('./app/static/oscar/less/*.less')
    .pipe(watch('./app/static/oscar/less/*.less'))
    .pipe(less({
      paths: [ path.join(__dirname, '/app/static/oscar/less/bootstrap') ]
     }))
    .pipe(gulp.dest('./app/static/oscar/css'));
});
