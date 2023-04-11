#include <progress2>

forward CreatePlayerProgressBar_py(playerid, Float:x, Float:y, Float:width, Float:height, colour, Float:max, progressbar_direction:direction);
public CreatePlayerProgressBar_py(playerid, Float:x, Float:y, Float:width, Float:height, colour, Float:max, progressbar_direction:direction)
{
	new Progress = _:CreatePlayerProgressBar(playerid, Float:x, Float:y, Float:width, Float:height, colour, Float:max, direction);
	return Progress;
}

forward DestroyPlayerProgressBar_py(playerid, PlayerBar:barid);
public DestroyPlayerProgressBar_py(playerid, PlayerBar:barid)
{
	DestroyPlayerProgressBar(playerid, PlayerBar:barid);
	return 1;
}


forward ShowPlayerProgressBar_py(playerid, PlayerBar:progressbar);
public ShowPlayerProgressBar_py(playerid, PlayerBar:progressbar)
{
	ShowPlayerProgressBar(playerid, progressbar);
	return 1;
}

forward HidePlayerProgressBar_py(playerid, PlayerBar:barid);
public HidePlayerProgressBar_py(playerid, PlayerBar:barid)
{
	HidePlayerProgressBar(playerid, PlayerBar:barid);
	return 1;
}

forward IsValidPlayerProgressBar_py(playerid, PlayerBar:barid);
public IsValidPlayerProgressBar_py(playerid, PlayerBar:barid)
{
	new isvalid = IsValidPlayerProgressBar(playerid, PlayerBar:barid);
	return isvalid;
}


forward GetPlayerProgressBarPos_py(playerid, PlayerBar:barid);
public GetPlayerProgressBarPos_py(playerid, PlayerBar:barid)
{
    new Float:pos[2];
    GetPlayerProgressBarPos(playerid, barid, pos[0], pos[1]);
    return floatround(pos[0] * 1000) | (floatround(pos[1] * 1000) << 16);
}

forward SetPlayerProgressBarPos_py(playerid, PlayerBar:barid, Float:x, Float:y);
public SetPlayerProgressBarPos_py(playerid, PlayerBar:barid, Float:x, Float:y)
{
	SetPlayerProgressBarPos(playerid, barid, x, y);
	return 1;
}

forward GetPlayerProgressBarWidth_py(playerid, PlayerBar:barid);
public GetPlayerProgressBarWidth_py(playerid, PlayerBar:barid)
{
	new Float:width = GetPlayerProgressBarWidth(playerid, barid);
	return floatround(width * 1000);
}

forward SetPlayerProgressBarWidth_py(playerid, PlayerBar:barid, Float:width);
public SetPlayerProgressBarWidth_py(playerid, PlayerBar:barid, Float:width)
{
	SetPlayerProgressBarWidth(playerid, barid, width);
	return 1;
}

forward Float:GetPlayerProgressBarHeight_py(playerid, PlayerBar:barid);
public Float:GetPlayerProgressBarHeight_py(playerid, PlayerBar:barid)
{
	new Float:height = GetPlayerProgressBarHeight(playerid, barid);
	return height;
}

forward SetPlayerProgressBarHeight_py(playerid, PlayerBar:barid, Float:height);
public SetPlayerProgressBarHeight_py(playerid, PlayerBar:barid, Float:height)
{
	SetPlayerProgressBarHeight(playerid, barid, height);
	return 1;
}

forward GetPlayerProgressBarColour_py(playerid, PlayerBar:barid);
public GetPlayerProgressBarColour_py(playerid, PlayerBar:barid)
{
	new colour = GetPlayerProgressBarColour(playerid, barid);
	return colour;
}

forward SetPlayerProgressBarColour_py(playerid, PlayerBar:barid, colour);
public SetPlayerProgressBarColour_py(playerid, PlayerBar:barid, colour)
{
	SetPlayerProgressBarColour(playerid, barid, colour);
	return 1;
}

forward Float:GetPlayerProgressBarMaxValue_py(playerid, PlayerBar:barid);
public Float:GetPlayerProgressBarMaxValue_py(playerid, PlayerBar:barid)
{
	new Float:maxx = GetPlayerProgressBarMaxValue(playerid, barid);
	return maxx;
}

forward SetPlayerProgressBarMaxValue_py(playerid, PlayerBar:barid, Float:max);
public SetPlayerProgressBarMaxValue_py(playerid, PlayerBar:barid, Float:max)
{
	SetPlayerProgressBarMaxValue(playerid, barid, max);
	return 1;
}

forward Float:GetPlayerProgressBarValue_py(playerid, PlayerBar:barid);
public Float:GetPlayerProgressBarValue_py(playerid, PlayerBar:barid)
{
	new Float:value = GetPlayerProgressBarValue(playerid, barid);
	return value;
}

forward SetPlayerProgressBarValue_py(playerid, PlayerBar:barid, Float:value);
public SetPlayerProgressBarValue_py(playerid, PlayerBar:barid, Float:value)
{
	SetPlayerProgressBarValue(playerid, barid, value);
	return 1;
}

forward GetPlayerProgressBarDirection_p(playerid, PlayerBar:barid);
public GetPlayerProgressBarDirection_p(playerid, PlayerBar:barid)
{
	new direction = _:GetPlayerProgressBarDirection(playerid, barid);
	return direction;
}

forward SetPlayerProgressBarDirection_p(playerid, PlayerBar:barid, progressbar_direction:direction);
public SetPlayerProgressBarDirection_p(playerid, PlayerBar:barid, progressbar_direction:direction)
{
	SetPlayerProgressBarDirection(playerid, barid, direction);
	return 1;
}