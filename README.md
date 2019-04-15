
<!DOCTYPE html>
<head>
    <title>Constituencywise-All Candidates</title>
    <meta http-equiv="Content-Language" content="en-us">
    
    <meta http-equiv="X-UA-Compatible" content="IE=7">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">
    <meta http-equiv="refresh" content="240">
    <!--<link rel="stylesheet" type="text/css" href="css/style.css"/>-->

    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
	<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
	<script type="text/javascript" src="javascript/TrendAnalysis.js"></script>
</head>
    
<body style="font-family: Verdana, Arial, Helvetica, sans-serif; font-size: 13px;
    width: 980px; padding: 0px; margin: auto;" bgcolor="#BFDAFB">
    <form name="aspnetForm">
         <div align="center">
            <table style="background-color: white;" width="960">
                <tbody>
                    <tr>
                        <td style="text-align: center" colspan="100">
                            <div style="font-size: 26px; font-weight: bold">
                                ELECTION COMMISSION OF INDIA
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td style="font-size: 16px; font-weight: bold; text-align: center">
                            GENERAL ELECTION TO VIDHAN SABHA TRENDS & RESULT 2018
                        </td>
                    </tr>
                    <tr>
                        <td valign="top" width="20%" style="font-weight: bolder;" align="center">
                            <br />
                            <div style="font-size: 12px">
                                Click links below for
                            </div>
                            <table id="ctl00_Menu1" class="ctl00_Menu1_2" cellpadding="0" cellspacing="0" border="0">
                                <tr>
                                   
                                    <td style="width: 3px;"></td>
                                    <td id="ctl00_Menu1n1">
                                        <table class="ctl00_Menu1_4" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td style="white-space: nowrap;">
                                                    <a class="ctl00_Menu1_1 ctl00_Menu1_3" href="/DADV/search.html">
                                                        Constituencywise-All-Candidates
                                                    </a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                    <td style="width: 3px;"></td>
                                    <td id="ctl00_Menu1n2">
                                        <table class="ctl00_Menu1_4" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td style="white-space: nowrap;">
                                                    
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                    <td style="width: 3px;"></td>
                                    <td id="ctl00_Menu1n2">
                                        <table class="ctl00_Menu1_4" cellpadding="0" cellspacing="0" border="0" width="100%">
                                            <tr>
                                                <td style="white-space: nowrap;">
                                                    <a class="ctl00_Menu1_1 ctl00_Menu1_3" href="trendwise_comparision_plot.html">Trends  </a>
                                                </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
        
        
        
        
            <table width="960px" style="background-color: White;">
                <tbody>
					
					
                <tr>
                    <td valign="top" width="80%">
                        <table style="margin: auto; width: 100%; font-family: Verdana; border: solid 1px black;
                        font-weight: lighter" id="id">
                            <tbody >
                            <tr>
                                <td colspan="2" align="center" style="font-size: large;">
                                    Constituencywise-All Candidates
                                </td>
                            </tr>
                            
                            <tr style="height: 20px; background-color: #BFDAFB; color: Black">
                                <td style="width: 50%; font-weight: 700;" colspan="2" align="center" >
                                    <b>Select State</b>
                                    <select name="ctl00$ContentPlaceHolder1$ACWise1$ddlState" onchange="stateChange()" id="selectS">
                                        <option value="">--select--</option>
                                        <option value="Chhattisgarh">Chhattisgarh</option>
                                        <option value="MadhyaPradesh">MadhyaPradesh</option>
                                        <option value="Mizoram">Mizoram</option>
                                        <option value="Rajasthan">Rajasthan</option>
                                        <option value="Telangana">Telangana</option>

                                    </select>
                                 
                                </td>
                            </tr>
                        </tbody></table>

                        <table width="100%">
                            <tbody><tr style="height: 10px">
                                <td></td>
                            </tr>
                            <tr>
                                <td align="center">
                                    <table width="50%">
                                        <tbody><tr>
                                            <td style="width: 100%">
                                                <div id="myDiv" style="width:1100px;height:600px;"></div>
                                            </td>
                                        </tr>
                                    </tbody></table>
                                </td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr>
                
                <tr style="height: 100px">
                    <td></td>
                </tr>
                <tr>
                    <td align="center">
                        <a href="">Disclaimer</a>
                    </td>
                </tr>
                
            </tbody></table>
            
    </form>
<div id="mySelector"></div>
	<table id="myTable"></table>
	
</body>
</html>
