var studentScheduleController = angular.module('studentScheduleController', []);

studentScheduleController.controller('monthCalCtrl', ['$scope',
	function($scope) {
		var month = [[1, 2, 3, 4, 5, 6, 7],
					 [1, 2, 3, 4, 5, 6, 7],
					 [1, 2, 3, 4, 5, 6, 7],
					 [1, 2, 3, 4, 5, 6, 7],
					 [1, 2, 3, 4, 5, 6, 7]];
		$scope.calTitle = "October"
		$scope.month = month;

		$scope.prev = function() {
			$scope.calTitle = "September";
			$scope.month = [[1, 2, 3, 4, 5, 6, 7],
					 [1, 2, 3, 4, 5, 6, 7],
					 [1, 2, 3, 4, 5, 6, 7],
					 [1, 2, 3, 4, 5, 6, 7],
					 [1, 2, 3, 4, 5, "", ""]];
		}

		$scope.next = function() {
			$scope.calTitle = "November";
			$scope.month = [[1, 2, 3, 4, 5, 6, 7],
					 [1, 2, 3, 4, 5, 6, 7],
					 [1, 2, 3, 4, 5, 6, 7],
					 [1, 2, 3, 4, 5, 6, 7],
					 [1, 2, 3, 4, 5, 6, ""]];
		}
	}
]);

studentScheduleController.controller('weekCalCtrl', ['$scope',
	function($scope) {
		$scope.calTitle = "Oct 1 to Oct 7";
		$scope.week = [1, 2, 3, 4, 5, 6, 7];

		$scope.next = function() {
			$scope.calTitle = "Oct 8 to Oct 14";
			$scope.week = [8, 9, 10, 11, 12, 13, 14];
		}

		$scope.prev = function() {
			$scope.calTitle = "Sept 24 to Sept 30";
			$scope.week = [24, 25, 26, 27, 28, 29, 30];
		}
	}
]);

studentScheduleController.controller('calTitle', ['$scope',
	function($scope) {
		$scope.title = "October"
	}
]);

studentScheduleController.controller('currentCalView', ['$scope', '$location',
	function($scope, $location) {
		$scope.location = $location;
	}
]);