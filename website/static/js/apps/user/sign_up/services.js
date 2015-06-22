angular.module( 'user.rest.sign_up' )
	factory( "rest.user",
	[ '$resource',
	function( $resource ) {
		return $resource( 'user',
			{},
			{
				save: {
					headers : {'Content-Type': 'application/x-www-form-urlencoded'}
					method : 'POST',
				}
			});
	} ] );
