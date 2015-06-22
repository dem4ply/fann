'use strict';
angular.module( 'user' )
	.factory( "rest.user",
	[ '$resource',
	function( $resource) {
		return $resource( '/api/user',
			{},
			{
				save: {
					headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
					method: 'POST'
				}
			} );
	} ] );
