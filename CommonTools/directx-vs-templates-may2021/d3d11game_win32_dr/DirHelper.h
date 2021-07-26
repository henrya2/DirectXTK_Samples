#pragma once

#include <string>
#include <Windows.h>

std::wstring GetExeDirectory()
{
	wchar_t buffer[MAX_PATH];
	GetModuleFileNameW(NULL, buffer, MAX_PATH);
	std::wstring::size_type pos = std::wstring(buffer).find_last_of(L"\\/");

	return std::wstring(buffer).substr(0, pos);
}

std::wstring GetProjDirectory()
{
	std::wstring ProjDir = GetExeDirectory() + +L"/" + L"../../../../..";

    return ProjDir;
}
