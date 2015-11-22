var app = angular.module("ussd", ['ngWebsocket', 'ngSanitize']);

app.controller("AppController", ["$scope", "$http", function($scope, $http){

	$scope.host = {"address": "127.0.0.1", "port": 15290};
	$scope.query_string = "1";
	$scope.ussdResponse = "<div class='muted text-center'>Response</div>";

	$scope.clear = function(){
		$scope.host = {"address": "", "port": null};
	};

	$scope.test = function(){

	};

	$scope.send = function(){
		console.log("send click");
		var server = "http://" + $scope.host.address + ":" + $scope.host.port;
		console.log(server);
		var data = {"server": server, "query_string": $scope.query_string};
		console.log("Request: ");
		console.log(data);
		$http({
		  method: 'GET',
		  url: '/ussdmenus/run',
		  params: data
		}).then(function successCallback(response) {
			// update UI with response
			console.log(response.data);
			$scope.ussdResponse = response.data;
			//$scope.$apply();
		}, function errorCallback(response) {
			// display notification
			console.log("error sending");
		});
	};
}]);