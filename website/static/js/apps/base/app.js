'use strict';
angular.module('base', [ 'ngCookies' ] )
	.config([
		'$httpProvider', '$interpolateProvider', 
		function($httpProvider, $interpolateProvider) {
			/*
			$interpolateProvider.startSymbol('{$');
			$interpolateProvider.endSymbol('$}');
			$httpProvider.defaults.headers.post['Content-Type']
				= 'application/x-www-form-urlencoded';
			*/
			$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
			$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		}
	])
	.run([
		'$http', '$cookies', 
		function($http, $cookies) {
			//console.log($cookies.getAll());
			//$http.defaults.headers.post['X-CSRFToken'] = $cookies.get( 'csrftoken' );
		}]);
