var studentScheduleApp = angular.module('studentScheduleApp', [
	'ngRoute',
	'studentScheduleController'
]);

studentScheduleApp.config(['$routeProvider',
	function($routeProvider, $location) {
		$routeProvider.when('/month', {
			templateUrl: 'static/partials/month.html',
			controller: 'monthCalCtrl'
		}).when('/week', {
			templateUrl: 'static/partials/week.html',
			controller: 'weekCalCtrl'
		}).otherwise({
			redirectTo: '/month'
		});
	}
]);