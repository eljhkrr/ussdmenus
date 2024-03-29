var app = angular.module("ussd", ['ngWebsocket', 'ngSanitize', 'xeditable']);

app.run(function(editableOptions) {
  editableOptions.theme = 'bs3';
});

app.controller("AppController", ["$scope", "$http", function($scope, $http){

	$scope.host = {"address": "127.0.0.1", "port": 15290};
	$scope.query_string = "1";
	
	$scope.ussdResponse = "<div class='text-muted text-center'>Response will be displayed here</div>";

	$scope.refresh = function(){
		$scope.msisdn = Math.floor((Math.random() * 1000000) + 1);;
		$scope.session_id = Math.floor((Math.random() * 1000000) + 1);
		$scope.imsi = Math.floor((Math.random() * 1000000) + 1);
	};

	$scope.test = function(){

	};

	$scope.send = function(){
		console.log("send click");
		var server = "http://" + $scope.host.address + ":" + $scope.host.port;
		console.log(server);
		var data = {"server": server, "query_string": $scope.query_string, "msisdn": $scope.msisdn, "session_id": $scope.session_id, "imsi": $scope.imsi};
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
			$scope.ussdResponse = "<div class='text-danger text-center'><i class='glyphicon glyphicon-warning-sign'></i> Error processing request. <br>Is the socket <kbd>" + $scope.host.address + ":" + $scope.host.port +"</kbd> alive?</div>";
		});
	};
}]);