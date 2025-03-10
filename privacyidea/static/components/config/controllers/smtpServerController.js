/**
 * http://www.privacyidea.org
 * (c) cornelius kölbel, cornelius@privacyidea.org
 *
 * 2015-12-28 Cornelius Kölbel, <cornelius@privacyidea.org>
 *
 * This code is free software; you can redistribute it and/or
 * modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
 * License as published by the Free Software Foundation; either
 * version 3 of the License, or any later version.
 *
 * This code is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU AFFERO GENERAL PUBLIC LICENSE for more details.
 *
 * You should have received a copy of the GNU Affero General Public
 * License along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */
myApp.controller("smtpServerController", ["$scope", "$stateParams", "inform",
    "gettextCatalog", "$state",
    "$location", "ConfigFactory",
    function ($scope, $stateParams, inform, gettextCatalog, $state, $location, ConfigFactory) {
        // set the default route
        if ($location.path() === "/config/smtp") {
            $location.path("/config/smtp/list");
        }
        $scope.identifier = $stateParams.identifier;
        $scope.params = {
                tls: true,
                port: 25,
                timeout: 10
            }

        // Get all servers
        $scope.getSmtpServers = function () {
            ConfigFactory.getSmtp(function (data) {
                $scope.smtpServers = data.result.value;
                //debug: console.log("Fetched all smtp servers");
                //debug: console.log($scope.smtpServers);
                // return one single smtp server
                if ($scope.identifier) {
                    // We are editing an existing SMTP Server
                    $scope.params = $scope.smtpServers[$scope.identifier];
                    $scope.params["identifier"] = $scope.identifier;
                }
                else {
                    // This is a new SMTP server
                    $scope.params = {
                        tls: true,
                        port: 25,
                        timeout: 10
                    };
                }
            });
        };

        if ($location.path() === "/config/smtp/list") {
            // in case of list we fetch all smtp servers
            $scope.getSmtpServers();
        }

        $scope.delSmtpServer = function (identifier) {
            ConfigFactory.delSmtp(identifier, function (data) {
                $scope.getSmtpServers();
            });
        };

        $scope.addSmtpServer = function (params) {
            ConfigFactory.addSmtp(params, function (data) {
                $scope.getSmtpServers();
            });
        };

        $scope.sendTestEmail = function () {
            ConfigFactory.testSmtp($scope.params, function (data) {
                if (data.result.value === true) {
                    inform.add(gettextCatalog.getString("Test Email sent" +
                            " successfully."),
                        {type: "info"});
                }
            });
        };

        $scope.saveSMTPServer = function () {
            ConfigFactory.addSmtp($scope.params, function (data) {
                if (data.result.status === true) {
                    inform.add(gettextCatalog.getString("SMTP Config saved."),
                        {type: "info"});
                    $scope.deselectSMTPServer();
                    $state.go('config.smtp.list');
                    $scope.reload();
                }
            });
        };

        $scope.deselectSMTPServer = function () {
            $scope.identifier = null;
            $scope.params = {
                tls: true,
                port: 25,
                timeout: 10
            };
            $scope.getSmtpServers();
        };

        $scope.editSMTPServer = function (identifier) {
            //$state.go('config.smtp.edit');
            $scope.identifier = identifier;
            $scope.getSmtpServers();
        };

        // listen to the reload broadcast
        $scope.$on("piReload", $scope.getSmtpServers);
    }]);
