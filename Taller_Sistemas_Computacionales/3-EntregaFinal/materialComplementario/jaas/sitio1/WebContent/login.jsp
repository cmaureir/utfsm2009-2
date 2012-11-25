<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8895-1">
<title>LOGIN</title>
</head>
<body>
<div id="layout">
<form method="post" action="j_security_check" name="j_security_check">
<table id="loginTable">
	<tbody>
		<tr>
			<td class="loginLabel"><span>Usuario</span></td>
			<td><input type="text" name="j_username" /></td>
		</tr>
		<tr>
			<td class="loginLabel"><span>Password</span></td>
			<td><input type="password" name="j_password" /></td>
		</tr>
		<tr>
			<td colspan="2"><input type="submit" value="Entrada al sistema" />
			</td>
		</tr>
	</tbody>
</table>
</form>
