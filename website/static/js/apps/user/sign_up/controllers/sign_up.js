'use strict';
angular.module( 'user.sign_up.ctrl' )
	.controller( 'user.sign_up.ctrl.sign_up',
	[ '$scope',
	function( $scope ) {
		$scope.models = {
			form: {
				first_name: '',
				last_name:'',
				password: '',
				email: ''
			}
		};

		$scope.on_register_manual = function() {
			console.log( $scope.models.form );
		};
		return $scope;
	} ] );
