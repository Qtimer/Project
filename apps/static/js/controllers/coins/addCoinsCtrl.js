app.controller("addCoinsCtrl", function ($scope, $window, $http, $rootScope) {
    $scope.mama = $rootScope.url;
    $scope.coin_transactions = [];
    var transactionTypeUsage = 0;

    $scope.getId = function (id) {
        $scope.sellerId = id;
        getProduct();
    };

     $scope.saveAddCoins = function (){
        var data = {
            account : $scope.sellerId,
            transaction_type : transactionTypeUsage,
            amount : $scope.amount,
        };

        $http.post($scope.mama + '/api/coin_transactions/', data).then(
            function success(response) {
                alert('เรียบร้อย')

            },
            function () {
                alert('fail')
            }

        )
    };
});