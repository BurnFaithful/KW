<%@ page import="youngmin.login.UserDAO" %>
<%@ page import="youngmin.login.UserDTO" %>
<% request.setCharacterEncoding("UTF-8"); %>
<%@ page language="java" contentType="text/html;charset=UTF-8"
         pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <%@ include file="file_header.jsp" %>
    <script src="../../js/page_func.js"></script>

    <script type="text/javascript">
        function openLearnmore()
        {
            var target = document.getElementById("main_learn_more");

            target.innerHTML = "<p>자세히 알아보기를 열었습니다.<br/> \
                                onclick() 테스트용으로 만들어봤습니다.<br/></p>";
        }

        function validate()
        {
            var userId = document.getElementById("login_userID");
            var userPw = document.getElementById("login_userPW");

            if (!userId.value || !userPw.value)
            {
                alert("입력되지 않은 사항이 있습니다.");
                return false;
            }

            return true;
        }
    </script>

    <title>영민이의 영화 채널</title>
</head>
<body>
<%@include file="page_header.jsp" %>
<script>
    checkPage("${param.pageName}");
</script>

<div class="container">
    <div class="jumbotron">
        <div class="container">
            <h1>영민이의 영화 채널</h1>
            <p>이 웹사이트는 부트스트랩, JSP, mySQL로 만든 영민이의 영화 채널입니다.</p>
            <button id ="main_btn_learn_more" class="btn btn-primary btn-pull" value="자세히 알아보기" onclick="openLearnmore()">자세히 알아보기</button>
            <div id="main_learn_more" class="text-info">
            </div>
        </div>
    </div>
</div>
<div class="container">
    <div class="row">
        <div class="col-lg-4">
            <div id="movieCarousel" class="carousel slide" data-ride="carousel">
                <ol class="carousel-indicators">
                    <li data-target="#movieCarousel" data-slide-to="0" class="active"></li>
                    <li data-target="#movieCarousel" data-slide-to="1"></li>
                    <li data-target="#movieCarousel" data-slide-to="2"></li>
                    <li data-target="#movieCarousel" data-slide-to="3"></li>
                    <li data-target="#movieCarousel" data-slide-to="4"></li>
                    <li data-target="#movieCarousel" data-slide-to="5"></li>
                </ol>
                <div class="carousel-inner">
                    <div class="item active">
                        <img src="../Image/darknight_poster.jpg" class="img-responsive" alt="">
                    </div>
                    <div class="item">
                        <img src="../Image/spiderman2_poster.jpg" class="img-responsive" alt="">
                    </div>
                    <div class="item">
                        <img src="../Image/thepursuitofhappiness_poster.jpg" class="img-responsive" alt="">
                    </div>
                    <div class="item">
                        <img src="../Image/threeidiots_poster.jpg" class="img-responsive" alt="">
                    </div>
                    <div class="item">
                        <img src="../Image/webaughtazoo_poster.jpg" class="img-responsive" alt="">
                    </div>
                    <div class="item">
                        <img src="../Image/abouttime_poster.jpg" class="img-responsive" alt="">
                    </div>
                </div>
                <a class="left carousel-control" href="#movieCarousel" data-slide="prev">
                    <span class="glyphicon glyphicon-chevron-left"></span>
                </a>
                <a class="right carousel-control" href="#movieCarousel" data-slide="next">
                    <span class="glyphicon glyphicon-chevron-right"></span>
                </a>
            </div>
        </div>
        <c:choose>
            <c:when test="${empty userID}">
        <div class="col-lg-4">
            <div class="jumbotron">
                <form method="post" action="login_Action.jsp" onsubmit="return validate()">
                    <h3 style="text-align: center;">로그인</h3>
                    <div class="form-group">
                        <input type="text" class="form-control" id="login_userID" name="userID" placeholder="아이디" maxlength="15"/>
                    </div>
                    <div class="form-group">
                        <input type="password" class="form-control" id="login_userPW" name="userPW" placeholder="비밀번호" maxlength="15"/>
                    </div>
                    <input type="submit" class="btn btn-primary form-control" value="로그인">
                </form>
            </div>
        </div>
            </c:when>
        <c:otherwise>
        <%
            String userID = pageContext.getAttribute("userID").toString();
            UserDTO userInfo = new UserDAO().getUserInfo(userID);
        %>
        <div class="col-lg-4">
            <h3 style="text-align: center">내 정보</h3>
            <table class="table table-bordered table-hover">
                <tr>
                    <td>아이디</td>
                    <td><%= userInfo.getUserID()%></td>
                </tr>
                <tr>
                    <td>이름</td>
                    <td><%= userInfo.getUserName()%></td>
                </tr>
                <tr>
                    <td>닉네임</td>
                    <td><%= userInfo.getUserNickname()%></td>
                </tr>
                <tr>
                    <td>전화번호</td>
                    <td><%= userInfo.getPhoneNumber()%></td>
                </tr>
                <tr>
                    <td>이메일</td>
                    <td><%= userInfo.getUserMail()%></td>
                </tr>
                <tr>
                    <td>성별</td>
                    <td><%= userInfo.getSex()%></td>
                </tr>
            </table>
        </div>
        </c:otherwise>
        </c:choose>
        <div class="col-lg-4">
            <div id="acterCarousel" class="carousel slide" data-ride="carousel">
                <ol class="carousel-indicators">
                    <li data-target="#acterCarousel" data-slide-to="0" class="active"></li>
                    <li data-target="#acterCarousel" data-slide-to="1"></li>
                    <li data-target="#acterCarousel" data-slide-to="2"></li>
                    <li data-target="#acterCarousel" data-slide-to="3"></li>
                    <li data-target="#acterCarousel" data-slide-to="4"></li>
                    <li data-target="#acterCarousel" data-slide-to="5"></li>
                </ol>
                <div class="carousel-inner">
                    <div class="item active">
                        <img src="../Image/천우희.jpg" class="img-responsive">
                    </div>
                    <div class="item">
                        <img src="../Image/신혜선.jpg" class="img-responsive">
                    </div>
                    <div class="item">
                        <img src="../Image/나가노메이.jpg" class="img-responsive">
                    </div>
                    <div class="item">
                        <img src="../Image/신예은.jpg" class="img-responsive">
                    </div>
                    <div class="item">
                        <img src="../Image/김옥빈.jpg" class="img-responsive">
                    </div>
                    <div class="item">
                        <img src="../Image/원진아.jpg" class="img-responsive">
                    </div>
                </div>
                <a class="left carousel-control" href="#acterCarousel" data-slide="prev">
                    <span class="glyphicon glyphicon-chevron-left"></span>
                </a>
                <a class="right carousel-control" href="#acterCarousel" data-slide="next">
                    <span class="glyphicon glyphicon-chevron-right"></span>
                </a>
            </div>
        </div>
    </div>
</div>

<%@include file="page_footer.jsp" %>
</body>
</html>
