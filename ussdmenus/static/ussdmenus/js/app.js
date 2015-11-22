var app = angular.module("ussd", ['ngWebsocket']);

app.controller("AppController", ["$scope", function($scope){

	$scope.host = {"address": "1.2.3.4", "port": 123};

	$scope.clear = function(){
		$scope.host = {"address": "", "port": null};
	};

	$scope.test = function(){};
}]);