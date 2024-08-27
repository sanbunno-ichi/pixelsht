import pyxel
#from font.bdfrenderer import BDFRenderer

################################################################################
#[const]定数

SCREEN_WIDTH	=	240
SCREEN_HEIGHT	=	320

ENE_YU_LIMIT	=	-30
ENE_YD_LIMIT	=	SCREEN_HEIGHT+30
ENE_XL_LIMIT	=	-20
ENE_XR_LIMIT	=	SCREEN_WIDTH+20

PLY_YU_LIMIT	=	0
PLY_YD_LIMIT	=	SCREEN_HEIGHT-8
PLY_XL_LIMIT	=	-8
PLY_XR_LIMIT	=	SCREEN_WIDTH-8

#-----------------------------------------------------------------
# game(game_adv)
G_TITLE			=	0
G_DEMOPLAY		=	1
G_GAME			=	2
G_OVER			=	3
G_STAGECLEAR	=	4
G_SETTING		=	5
G_DEBUG			=	6
G_END			=	7

################################################################################
#[workass]変数
_ass = 0
GWK = [0 for _ass in range(0x1000)]	#変数管理
WORK_TOP		=	0
WORK_END		=	0x1000
#-----------------------------------------------------------------
W_PAGE00		=	WORK_TOP+0x0000
W_PAGE01		=	WORK_TOP+0x0100
W_PAGE02		=	WORK_TOP+0x0200
W_PAGE03		=	WORK_TOP+0x0300
W_PAGE04		=	WORK_TOP+0x0400
W_PAGE05		=	WORK_TOP+0x0500
W_PAGE06		=	WORK_TOP+0x0600
W_PAGE07		=	WORK_TOP+0x0700
W_PAGE08		=	WORK_TOP+0x0800
W_PAGE09		=	WORK_TOP+0x0900
W_PAGE0a		=	WORK_TOP+0x0a00
W_PAGE0b		=	WORK_TOP+0x0b00
W_PAGE0c		=	WORK_TOP+0x0c00
W_PAGE0d		=	WORK_TOP+0x0d00
W_PAGE0e		=	WORK_TOP+0x0e00
W_PAGE0f		=	WORK_TOP+0x0f00

#-----------------------------------------------------------------
#	PAGE00
#-----------------------------------------------------------------
game_adv		=	W_PAGE00+0x00		#game_control number


ene_g1_number	=	W_PAGE00+0x10		#enemy group1 順番番号
ene_g2_number	=	W_PAGE00+0x11		#enemy group2 順番番号
ene_g3_number	=	W_PAGE00+0x12		#enemy group3 順番番号

#-----------------------------------------------------------------
cid			=	0x00		#ID番号
ccond		=	0x01		#状態フラグ
#状態フラグ内訳
F_LIVE			=	0x01		#[bit0]生(1)死(0)
F_ACTIVE		=	0x02		#[bit1]アクティブ
F_HIT			=	0x04		#[bit2]ヒット！(1)無し(0)
F_CRASH			=	0x08		#[bit3]爆発中(1)無し(0)
F_WARP			=	0x08		#[bit3]ワープ（星用）
F_WARPEND		=	0x10		#[bit4]ワープ終了（星用）

cxpos		=	0x02		#X座標
cypos		=	0x03		#Y座標
cxspd		=	0x04		#X移動スピード
cyspd		=	0x05		#Y移動スピード

canum		=	0x06		#アニメ番号
cacnt		=	0x07		#アニメカウンタ
caspd		=	0x08		#アニメスピードカウンタ

cmnum		=	0x09		#移動パターン番号
cmcnt		=	0x0a		#移動カウンタ
cmcnt2		=	0x0b		#移動カウンタ２
cwait		=	0x0c		#登場待ちカウンタ

CHAR_MAX		=	0x10		#character ass max

#-----------------------------------------------------------------
#	PAGE01	プレイヤー他
#-----------------------------------------------------------------
PLY_WORK		=	W_PAGE01+0x00

#-----------------------------------------------------------------
#	PAGE02,03	プレイヤーの弾
#-----------------------------------------------------------------
PT_WORK			=	W_PAGE02+0x00
PTMAX			=	32
#-----------------------------------------------------------------
#	PAGE04,05,06,07	星
#-----------------------------------------------------------------
STARMAX			=	32
STAR1_WORK		=	W_PAGE04+0x00						#手前側
STAR2_WORK		=	STAR1_WORK + ( CHAR_MAX * STARMAX )	#奥側
#-----------------------------------------------------------------
#	PAGE08	敵グループ１
#-----------------------------------------------------------------
ENE_WORK		=	W_PAGE08+0x00
#ENE_G1_WORK	=	W_PAGE08+0x00
ENE_G1_WORK		=	ENE_WORK
ENE_G1_MAX		=	16
#-----------------------------------------------------------------
#	PAGE09	敵グループ２
#-----------------------------------------------------------------
#ENE_G2_WORK	=	W_PAGE09+0x00
ENE_G2_WORK		=	ENE_WORK + ( CHAR_MAX * ENE_G1_MAX )
ENE_G2_MAX		=	16
#-----------------------------------------------------------------
#	PAGE0a	敵グループ３
#-----------------------------------------------------------------
#ENE_G3_WORK	=	W_PAGE0a+0x00
ENE_G3_WORK		=	ENE_WORK + ( CHAR_MAX * ENE_G2_MAX )
ENE_G3_MAX		=	16
#-----------------------------------------------------------------
#	PAGE0b
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#キャラクタテーブル
#-----------------------------------------------------------------
IDMAX = 0x8c
ctbl = [[0 for i in range(4)] for j in range(IDMAX)]
ctbl = [
	# u,    v,    us,   vs
	[ 0x00, 0xa0, 0x01, 0x01 ],		#0x00 明るい星1
	[ 0x04, 0xa0, 0x01, 0x01 ],		#0x01 暗い星1
	[ 0x00, 0x08, 0x02, 0x02 ],		#0x02 敵弾1-1(2x2)
	[ 0x04, 0x08, 0x02, 0x02 ],		#0x03 敵弾1-2
	[ 0x00, 0x0c, 0x02, 0x02 ],		#0x04 敵弾1-3
	[ 0x04, 0x0c, 0x02, 0x02 ],		#0x05 敵弾1-4
	[ 0x00, 0x70, 0x08, 0x0a ],		#0x06 敵弾2-1(8x10)
	[ 0x08, 0x70, 0x08, 0x0a ],		#0x07 敵弾2-2
	[ 0x10, 0x70, 0x08, 0x0a ],		#0x08 敵弾2-3
	[ 0x18, 0x70, 0x08, 0x0a ],		#0x09 敵弾2-4
	[ 0x20, 0x70, 0x08, 0x0a ],		#0x0a 敵弾3-1(8x10)
	[ 0x28, 0x70, 0x08, 0x0a ],		#0x0b 敵弾3-2
	[ 0x30, 0x70, 0x08, 0x0a ],		#0x0c 敵弾3-3
	[ 0x38, 0x70, 0x08, 0x0a ],		#0x0d 敵弾3-4
	[ 0x40, 0x70, 0x08, 0x0a ],		#0x0e 敵弾4-1(8x10)
	[ 0x48, 0x70, 0x08, 0x0a ],		#0x0f 敵弾4-2
	[ 0x50, 0x70, 0x08, 0x0a ],		#0x10 敵弾4-3
	[ 0x58, 0x70, 0x08, 0x0a ],		#0x11 敵弾4-4
	[ 0x60, 0x70, 0x08, 0x0a ],		#0x12 自弾1-1(8x10)
	[ 0x68, 0x70, 0x08, 0x0a ],		#0x13 自弾1-2
	[ 0x70, 0x70, 0x08, 0x0a ],		#0x14 自弾1-3
	[ 0x78, 0x70, 0x08, 0x0a ],		#0x15 自弾1-4
	[ 0x60, 0x70, 0x08, 0x05 ],		#0x16 インベ自弾2-1(8x5)
	[ 0x00, 0x00, 0x00, 0x00 ],		#0x17 (空)

	[ 0x00, 0x58, 0x10, 0x08 ],		#0x18 インベ自機(白)
	[ 0x10, 0x58, 0x10, 0x08 ],		#0x19 インベ自機(赤)
	[ 0x20, 0x58, 0x10, 0x08 ],		#0x1a インベ自機(青)
	[ 0x30, 0x58, 0x10, 0x08 ],		#0x1b インベ自機(緑)
	[ 0x40, 0x58, 0x10, 0x08 ],		#0x1c インベ自機(黄)
	[ 0x50, 0x58, 0x10, 0x08 ],		#0x1d インベ自機(桃)
	[ 0x60, 0x58, 0x10, 0x08 ],		#0x1e インベ自機(紫)
	[ 0x70, 0x58, 0x10, 0x10 ],		#0x1f インベ自機(灰)
	[ 0x00, 0x60, 0x10, 0x10 ],		#0x20 自機(白)
	[ 0x10, 0x60, 0x10, 0x10 ],		#0x21 自機(赤)
	[ 0x20, 0x60, 0x10, 0x10 ],		#0x22 自機(青)
	[ 0x30, 0x60, 0x10, 0x10 ],		#0x23 自機(緑)
	[ 0x40, 0x60, 0x10, 0x10 ],		#0x24 自機(黄)
	[ 0x50, 0x60, 0x10, 0x10 ],		#0x25 自機(桃)
	[ 0x60, 0x60, 0x10, 0x10 ],		#0x26 自機(紫)
	[ 0x70, 0x60, 0x10, 0x10 ],		#0x27 自機(灰)

	[ 0x00, 0x10, 0x10, 0x08 ],		#0x28 敵1-1-1(白)
	[ 0x00, 0x18, 0x10, 0x08 ],		#0x29 敵1-1-2(白)
	[ 0x10, 0x10, 0x10, 0x08 ],		#0x2a 敵1-2-1(赤)
	[ 0x10, 0x18, 0x10, 0x08 ],		#0x2b 敵1-2-2(赤)
	[ 0x20, 0x10, 0x10, 0x08 ],		#0x2c 敵1-3-1(青)
	[ 0x20, 0x18, 0x10, 0x08 ],		#0x2d 敵1-3-2(青)
	[ 0x30, 0x10, 0x10, 0x08 ],		#0x2e 敵1-4-1(緑)
	[ 0x30, 0x18, 0x10, 0x08 ],		#0x2f 敵1-4-2(緑)
	[ 0x40, 0x10, 0x10, 0x08 ],		#0x30 敵1-5-1(黄)
	[ 0x40, 0x18, 0x10, 0x08 ],		#0x31 敵1-5-2(黄)
	[ 0x50, 0x10, 0x10, 0x08 ],		#0x32 敵1-6-1(桃)
	[ 0x50, 0x18, 0x10, 0x08 ],		#0x33 敵1-6-2(桃)
	[ 0x60, 0x10, 0x10, 0x08 ],		#0x34 敵1-7-1(紫)
	[ 0x60, 0x18, 0x10, 0x08 ],		#0x35 敵1-7-2(紫)
	[ 0x70, 0x10, 0x10, 0x08 ],		#0x36 敵1-8-1(灰)
	[ 0x70, 0x18, 0x10, 0x08 ],		#0x37 敵1-8-2(灰)

	[ 0x00, 0x20, 0x10, 0x08 ],		#0x38 敵2-1-1(白)
	[ 0x00, 0x28, 0x10, 0x08 ],		#0x39 敵2-1-2(白)
	[ 0x10, 0x20, 0x10, 0x08 ],		#0x3a 敵2-2-1(赤)
	[ 0x10, 0x28, 0x10, 0x08 ],		#0x3b 敵2-2-2(赤)
	[ 0x20, 0x20, 0x10, 0x08 ],		#0x3c 敵2-3-1(青)
	[ 0x20, 0x28, 0x10, 0x08 ],		#0x3d 敵2-3-2(青)
	[ 0x30, 0x20, 0x10, 0x08 ],		#0x3e 敵2-4-1(緑)
	[ 0x30, 0x28, 0x10, 0x08 ],		#0x3f 敵2-4-2(緑)
	[ 0x40, 0x20, 0x10, 0x08 ],		#0x40 敵2-5-1(黄)
	[ 0x40, 0x28, 0x10, 0x08 ],		#0x41 敵2-5-2(黄)
	[ 0x50, 0x20, 0x10, 0x08 ],		#0x42 敵2-6-1(桃)
	[ 0x50, 0x28, 0x10, 0x08 ],		#0x43 敵2-6-2(桃)
	[ 0x60, 0x20, 0x10, 0x08 ],		#0x44 敵2-7-1(紫)
	[ 0x60, 0x28, 0x10, 0x08 ],		#0x45 敵2-7-2(紫)
	[ 0x70, 0x20, 0x10, 0x08 ],		#0x46 敵2-8-1(灰)
	[ 0x70, 0x28, 0x10, 0x08 ],		#0x47 敵2-8-2(灰)

	[ 0x00, 0x30, 0x10, 0x08 ],		#0x48 敵3-1-1(白)
	[ 0x00, 0x38, 0x10, 0x08 ],		#0x49 敵3-1-2(白)
	[ 0x10, 0x30, 0x10, 0x08 ],		#0x4a 敵3-2-1(赤)
	[ 0x10, 0x38, 0x10, 0x08 ],		#0x4b 敵3-2-2(赤)
	[ 0x20, 0x30, 0x10, 0x08 ],		#0x4c 敵3-3-1(青)
	[ 0x20, 0x38, 0x10, 0x08 ],		#0x4d 敵3-3-2(青)
	[ 0x30, 0x30, 0x10, 0x08 ],		#0x4e 敵3-4-1(緑)
	[ 0x30, 0x38, 0x10, 0x08 ],		#0x4f 敵3-4-2(緑)
	[ 0x40, 0x30, 0x10, 0x08 ],		#0x50 敵3-5-1(黄)
	[ 0x40, 0x38, 0x10, 0x08 ],		#0x51 敵3-5-2(黄)
	[ 0x50, 0x30, 0x10, 0x08 ],		#0x52 敵3-6-1(桃)
	[ 0x50, 0x38, 0x10, 0x08 ],		#0x53 敵3-6-2(桃)
	[ 0x60, 0x30, 0x10, 0x08 ],		#0x54 敵3-7-1(紫)
	[ 0x60, 0x38, 0x10, 0x08 ],		#0x55 敵3-7-2(紫)
	[ 0x70, 0x30, 0x10, 0x08 ],		#0x56 敵3-8-1(灰)
	[ 0x70, 0x38, 0x10, 0x08 ],		#0x57 敵3-8-2(灰)

	[ 0x00, 0x40, 0x10, 0x08 ],		#0x58 UFO-1-1(白)
	[ 0x00, 0x48, 0x10, 0x08 ],		#0x59 UFO-1-2(白)
	[ 0x00, 0x50, 0x10, 0x08 ],		#0x5a UFO-1-3(白)
	[ 0x10, 0x40, 0x10, 0x08 ],		#0x5b UFO-2-1(赤)
	[ 0x10, 0x48, 0x10, 0x08 ],		#0x5c UFO-2-2(赤)
	[ 0x10, 0x50, 0x10, 0x08 ],		#0x5d UFO-2-3(赤)
	[ 0x20, 0x40, 0x10, 0x08 ],		#0x5e UFO-3-1(青)
	[ 0x20, 0x48, 0x10, 0x08 ],		#0x5f UFO-3-2(青)
	[ 0x20, 0x50, 0x10, 0x08 ],		#0x60 UFO-3-3(青)
	[ 0x30, 0x40, 0x10, 0x08 ],		#0x61 UFO-4-1(緑)
	[ 0x30, 0x48, 0x10, 0x08 ],		#0x62 UFO-4-2(緑)
	[ 0x30, 0x50, 0x10, 0x08 ],		#0x63 UFO-4-3(緑)
	[ 0x40, 0x40, 0x10, 0x08 ],		#0x64 UFO-5-1(黄)
	[ 0x40, 0x48, 0x10, 0x08 ],		#0x65 UFO-5-2(黄)
	[ 0x40, 0x50, 0x10, 0x08 ],		#0x66 UFO-5-3(黄)
	[ 0x50, 0x40, 0x10, 0x08 ],		#0x67 UFO-6-1(桃)
	[ 0x50, 0x48, 0x10, 0x08 ],		#0x68 UFO-6-2(桃)
	[ 0x50, 0x50, 0x10, 0x08 ],		#0x69 UFO-6-3(桃)
	[ 0x60, 0x40, 0x10, 0x08 ],		#0x6a UFO-7-1(紫)
	[ 0x60, 0x48, 0x10, 0x08 ],		#0x6b UFO-7-2(紫)
	[ 0x60, 0x50, 0x10, 0x08 ],		#0x6c UFO-7-3(紫)
	[ 0x70, 0x40, 0x10, 0x08 ],		#0x6d UFO-8-1(灰)
	[ 0x70, 0x48, 0x10, 0x08 ],		#0x6e UFO-8-2(灰)
	[ 0x70, 0x50, 0x10, 0x08 ],		#0x6f UFO-8-3(灰)

	[ 0x00, 0x80, 0x10, 0x10 ],		#0x70 爆発赤1
	[ 0x10, 0x80, 0x10, 0x10 ],		#0x71 爆発赤2
	[ 0x00, 0x90, 0x10, 0x10 ],		#0x72 爆発赤3
	[ 0x10, 0x90, 0x10, 0x10 ],		#0x73 爆発赤4

	[ 0x20, 0x80, 0x10, 0x10 ],		#0x74 爆発白1
	[ 0x30, 0x80, 0x10, 0x10 ],		#0x75 爆発白2
	[ 0x20, 0x90, 0x10, 0x10 ],		#0x76 爆発白3
	[ 0x30, 0x90, 0x10, 0x10 ],		#0x77 爆発白4

	[ 0x08, 0x00, 0x08, 0x08 ],		#0x78 SpeedUp(灰)
	[ 0x10, 0x00, 0x08, 0x08 ],		#0x79 SpeedUp(赤)
	[ 0x18, 0x00, 0x08, 0x08 ],		#0x7a SpeedUp(黄)
	[ 0x20, 0x00, 0x08, 0x08 ],		#0x7b SpeedUp(緑)
	[ 0x28, 0x00, 0x08, 0x08 ],		#0x7c SpeedUp(青)
	[ 0x30, 0x00, 0x08, 0x08 ],		#0x7d SpeedUp(白)

	[ 0x08, 0x08, 0x08, 0x08 ],		#0x7e PowerUp(灰)
	[ 0x10, 0x08, 0x08, 0x08 ],		#0x7f PowerUp(赤)
	[ 0x18, 0x08, 0x08, 0x08 ],		#0x80 PowerUp(黄)
	[ 0x20, 0x08, 0x08, 0x08 ],		#0x81 PowerUp(緑)
	[ 0x28, 0x08, 0x08, 0x08 ],		#0x82 PowerUp(青)
	[ 0x30, 0x08, 0x08, 0x08 ],		#0x83 PowerUp(白)

	[ 0x08, 0xa0, 0x01, 0x02 ],		#0x84 明るい星2
	[ 0x10, 0xa0, 0x01, 0x04 ],		#0x85 明るい星3
	[ 0x18, 0xa0, 0x01, 0x08 ],		#0x86 明るい星4
	[ 0x20, 0xa0, 0x01, 0x10 ],		#0x87 明るい星5

	[ 0x0c, 0xa0, 0x01, 0x02 ],		#0x88 暗い星2
	[ 0x14, 0xa0, 0x01, 0x04 ],		#0x89 暗い星3
	[ 0x1c, 0xa0, 0x01, 0x08 ],		#0x8a 暗い星4
	[ 0x24, 0xa0, 0x01, 0x10 ],		#0x8b 暗い星5
]

#-----------------------------------------------------------------
#アニメテーブル（内容はキャラクタID、６パターン以上は別途・・・
#-----------------------------------------------------------------
ANIMMAX = 0x2c
atbl = [[0 for i in range(8)] for j in range(ANIMMAX)]
atbl = [
	#spd,p1,,,0xff(終端)（spd=0はアニメ無し）
	[ 2, 0x02, 0x03, 0x04, 0x05, 0xff, 0xff, 0xff ],		#0x00 敵弾1(2x2)
	[ 2, 0x06, 0x07, 0x08, 0x09, 0xff, 0xff, 0xff ],		#0x01 敵弾2(8x10)
	[ 2, 0x0a, 0x0b, 0x0c, 0x0d, 0xff, 0xff, 0xff ],		#0x02 敵弾3(8x10)
	[ 2, 0x0e, 0x0f, 0x10, 0x11, 0xff, 0xff, 0xff ],		#0x03 敵弾4(8x10)
	[ 4, 0x12, 0x13, 0x14, 0x15, 0xff, 0xff, 0xff ],		#0x04 自弾1(8x10)
	[ 0, 0x16, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x05 自弾2(8x5)

	[ 8, 0x28, 0x29, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x06 敵1-1(白)(16x8)
	[ 8, 0x2a, 0x2b, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x07 敵1-2(赤)(16x8)
	[ 8, 0x2c, 0x2d, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x08 敵1-3(青)(16x8)
	[ 8, 0x2e, 0x2f, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x09 敵1-4(緑)(16x8)
	[ 8, 0x30, 0x31, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x0a 敵1-5(黄)(16x8)
	[ 8, 0x32, 0x33, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x0b 敵1-6(桃)(16x8)
	[ 8, 0x34, 0x35, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x0c 敵1-7(紫)(16x8)
	[ 8, 0x36, 0x37, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x0d 敵1-8(灰)(16x8)

	[ 8, 0x38, 0x39, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x0e 敵2-1(白)(16x8)
	[ 8, 0x3a, 0x3b, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x0f 敵2-2(赤)(16x8)
	[ 8, 0x3c, 0x3d, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x10 敵2-3(青)(16x8)
	[ 8, 0x3e, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x11 敵2-4(緑)(16x8)
	[ 8, 0x40, 0x41, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x12 敵2-5(黄)(16x8)
	[ 8, 0x42, 0x43, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x13 敵2-6(桃)(16x8)
	[ 8, 0x44, 0x45, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x14 敵2-7(紫)(16x8)
	[ 8, 0x46, 0x47, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x15 敵2-8(灰)(16x8)

	[ 8, 0x48, 0x49, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x16 敵3-1(白)(16x8)
	[ 8, 0x4a, 0x4b, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x17 敵3-2(赤)(16x8)
	[ 8, 0x4c, 0x4d, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x18 敵3-3(青)(16x8)
	[ 8, 0x4e, 0x4f, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x19 敵3-4(緑)(16x8)
	[ 8, 0x50, 0x51, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x1a 敵3-5(黄)(16x8)
	[ 8, 0x52, 0x53, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x1b 敵3-6(桃)(16x8)
	[ 8, 0x54, 0x55, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x1c 敵3-7(紫)(16x8)
	[ 8, 0x56, 0x57, 0xff, 0xff, 0xff, 0xff, 0xff ],		#0x1d 敵3-8(灰)(16x8)

	[ 8, 0x58, 0x59, 0x5a, 0xff, 0xff, 0xff, 0xff ],		#0x1e UFO-1(白)(16x8)
	[ 8, 0x5b, 0x5c, 0x5d, 0xff, 0xff, 0xff, 0xff ],		#0x1f UFO-2(赤)(16x8)
	[ 8, 0x5e, 0x5f, 0x60, 0xff, 0xff, 0xff, 0xff ],		#0x20 UFO-3(青)(16x8)
	[ 8, 0x61, 0x62, 0x63, 0xff, 0xff, 0xff, 0xff ],		#0x21 UFO-4(緑)(16x8)
	[ 8, 0x64, 0x65, 0x66, 0xff, 0xff, 0xff, 0xff ],		#0x22 UFO-5(黄)(16x8)
	[ 8, 0x67, 0x68, 0x69, 0xff, 0xff, 0xff, 0xff ],		#0x23 UFO-6(桃)(16x8)
	[ 8, 0x6a, 0x6b, 0x6c, 0xff, 0xff, 0xff, 0xff ],		#0x24 UFO-7(紫)(16x8)
	[ 8, 0x6d, 0x6e, 0x6f, 0xff, 0xff, 0xff, 0xff ],		#0x25 UFO-8(灰)(16x8)

	[ 4, 0x70, 0x71, 0x72, 0x73, 0xff, 0xff, 0xff ],		#0x26 爆発赤(16x16)
	[ 4, 0x74, 0x75, 0x76, 0x77, 0xff, 0xff, 0xff ],		#0x27 爆発白(16x16)

	[ 1, 0x78, 0x79, 0x7a, 0x7b, 0x7c, 0x7d, 0xff ],		#0x28 SpeedUp(8x8)
	[ 1, 0x7e, 0x7f, 0x80, 0x81, 0x82, 0x83, 0xff ],		#0x29 PowerUp(8x8)

	[ 4, 0x00, 0x84, 0x85, 0x86, 0x87, 0xff, 0xff ],		#0x2a 明るい星ワープ(1x1～16)
	[ 4, 0x01, 0x88, 0x89, 0x8a, 0x8b, 0xff, 0xff ],		#0x2b 暗い星ワープ(1x1～16)
]

#-----------------------------------------------------------------
#アニメーション制御
#	_flag	0:通常ループ実行
#			1:終端で終了（戻り値1で終了）
#			2:終端から逆実行、最初に戻って終了（戻り値1で終了）
#-----------------------------------------------------------------
def anim_control( _wk, _flag ):
	#アニメ番号有り
	if( GWK[_wk+canum] < ANIMMAX ):
		GWK[_wk+caspd] += 1
		#アニメスピード超えた？
		if( GWK[_wk+caspd] >= atbl[GWK[_wk+canum]][0] ):
			GWK[_wk+caspd] = 0

			if( _flag == 0 ):
				GWK[_wk+cacnt] += 1
				#アニメ終端？
				if( atbl[GWK[_wk+canum]][GWK[_wk+cacnt]+1] == 0xff ):
					GWK[_wk+cacnt] = 0
			elif( _flag == 1 ):
				GWK[_wk+cacnt] += 1
				#アニメ終端？
				if( atbl[GWK[_wk+canum]][GWK[_wk+cacnt]+1] == 0xff ):
					GWK[_wk+cacnt] -= 1		#終端前に戻す
					return (1)
			elif( _flag == 2 ):
				GWK[_wk+cacnt] -= 1
				#アニメ始端？
				if( GWK[_wk+cacnt] < 0 ):
					GWK[_wk+cacnt] = 0
					return (1)
	return (0)

#-----------------------------------------------------------------
#プレイヤーの弾
#-----------------------------------------------------------------
#	弾生成
def ptama_set():
	for _cnt in range(PTMAX):
		_wk = PT_WORK+(CHAR_MAX * _cnt)
		if(( GWK[_wk+ccond] & F_LIVE ) == 0 ):
			GWK[_wk+cid] = 0x12		#0x16
			GWK[_wk+cxpos] = GWK[PLY_WORK+cxpos]+4
			GWK[_wk+cypos] = GWK[PLY_WORK+cypos]-4
			GWK[_wk+cxspd] = 0
			GWK[_wk+cyspd] = -6
			GWK[_wk+canum] = 0x04	#0
			GWK[_wk+cacnt] = 0
			GWK[_wk+caspd] = 0
			GWK[_wk+ccond] = F_LIVE
			break

#-----------------------------------------------------------------
#	弾制御
def ptama_control():
	for _cnt in range(PTMAX):
		_wk = PT_WORK+(CHAR_MAX * _cnt)
		if( GWK[_wk+ccond] & F_LIVE ):
			anim_control( _wk, 0 )
			GWK[_wk+cypos] += GWK[_wk+cyspd]
			if( GWK[_wk+cypos] < -30 ):
				GWK[_wk+ccond] = GWK[_wk+ccond] & ~F_LIVE

#-----------------------------------------------------------------
#	弾描画
def ptama_draw():
	for _cnt in range(PTMAX):
		_wk = PT_WORK+(CHAR_MAX * _cnt)
		if( GWK[_wk+ccond] & F_LIVE ):
			if( GWK[_wk+canum] != 0xff ):
				_id = atbl[GWK[_wk+canum]][GWK[_wk+cacnt]+1]
			else:
				_id = GWK[_wk+cid]
			_xp = GWK[_wk+cxpos]
			_yp = GWK[_wk+cypos]
			pyxel.blt( _xp, _yp, 0, ctbl[_id][0], ctbl[_id][1], ctbl[_id][2], ctbl[_id][3], 0 )

#-----------------------------------------------------------------
#星
#-----------------------------------------------------------------
#	初期設定：登場待ち時間設定
def star_init():
	_pos_range = int(SCREEN_WIDTH / STARMAX)
	_pos_offset = 0
	for _cnt in range(STARMAX):
		#手前側
		_pos_offset = pyxel.rndi(0, _pos_range)
		_wk = STAR1_WORK+(CHAR_MAX * _cnt)
		GWK[_wk+cxpos] = ( _cnt * _pos_range ) + _pos_offset
		GWK[_wk+cypos] = -30
		GWK[_wk+cxspd] = 0.0
		GWK[_wk+cyspd] = 2.0
		GWK[_wk+cwait] = pyxel.rndi(0, SCREEN_HEIGHT)
		GWK[_wk+cid] = 0x00
		GWK[_wk+ccond] = 0x00
		GWK[_wk+canum] = 0xff
		GWK[_wk+cacnt] = 0
		GWK[_wk+caspd] = 0
		#奥側
		_pos_offset = pyxel.rndi(0, _pos_range)
		_wk = STAR2_WORK+(CHAR_MAX * _cnt)
		GWK[_wk+cxpos] = ( _cnt * _pos_range ) + _pos_offset
		GWK[_wk+cypos] = -30
		GWK[_wk+cxspd] = 0.0
		GWK[_wk+cyspd] = 1.0
		GWK[_wk+cwait] = pyxel.rndi(0, SCREEN_HEIGHT)
		GWK[_wk+cid] = 0x01
		GWK[_wk+ccond] = 0x00
		GWK[_wk+canum] = 0xff
		GWK[_wk+cacnt] = 0
		GWK[_wk+caspd] = 0

#-----------------------------------------------------------------
#星制御
def star_control():
	_pos_range = int(SCREEN_WIDTH / STARMAX)
	for _cnt in range(STARMAX):
		#手前側
		_wk = STAR1_WORK+(CHAR_MAX * _cnt)
		#ワープ制御
		if( GWK[_wk+ccond] & F_WARPEND ):
			if anim_control( _wk, 2 ):
				GWK[_wk+cyspd] = 2.0
				GWK[_wk+cid] = 0x00
				GWK[_wk+canum] = 0xff
				GWK[_wk+cacnt] = 0
				GWK[_wk+caspd] = 0
				GWK[_wk+ccond] &= ~(F_WARP+F_WARPEND)
		elif( GWK[_wk+ccond] & F_WARP ):
			if anim_control( _wk, 1 ):
				GWK[_wk+cyspd] = 8.0
		else:
			if( GWK[_wk+ccond] & F_LIVE ):
				anim_control( _wk, 0 )
		#移動
		if( GWK[_wk+ccond] & F_LIVE ):
			GWK[_wk+cypos] += GWK[_wk+cyspd]
			if( GWK[_wk+cypos] > (SCREEN_HEIGHT+10) ):
				GWK[_wk+ccond] = GWK[_wk+ccond] & ~F_LIVE
				_pos_offset = pyxel.rndi(0, _pos_range)
				GWK[_wk+cxpos] = ( _cnt * _pos_range ) + _pos_offset
				GWK[_wk+cwait] = pyxel.rndi(0, SCREEN_HEIGHT)
				GWK[_wk+cypos] = -30
		else:
			GWK[_wk+cwait] -= 1
			if( GWK[_wk+cwait] < 0 ):
				GWK[_wk+ccond] |= F_LIVE

		#奥側
		_wk = STAR2_WORK+(CHAR_MAX * _cnt)
		#ワープ制御
		if( GWK[_wk+ccond] & F_WARPEND ):
			if anim_control( _wk, 2 ):
				GWK[_wk+cyspd] = 1.0
				GWK[_wk+cid] = 0x01
				GWK[_wk+canum] = 0xff
				GWK[_wk+cacnt] = 0
				GWK[_wk+caspd] = 0
				GWK[_wk+ccond] &= ~(F_WARP+F_WARPEND)
		elif( GWK[_wk+ccond] & F_WARP ):
			if anim_control( _wk, 1 ):
				GWK[_wk+cyspd] = 4.0
		else:
			if( GWK[_wk+ccond] & F_LIVE ):
				anim_control( _wk, 0 )
		#移動
		if( GWK[_wk+ccond] & F_LIVE ):
			GWK[_wk+cypos] += GWK[_wk+cyspd]
			if( GWK[_wk+cypos] > (SCREEN_HEIGHT+10) ):
				GWK[_wk+ccond] = GWK[_wk+ccond] & ~F_LIVE
				_pos_offset = pyxel.rndi(0, _pos_range)
				GWK[_wk+cxpos] = ( _cnt * _pos_range ) + _pos_offset
				GWK[_wk+cwait] = pyxel.rndi(0, SCREEN_HEIGHT)
				GWK[_wk+cypos] = -30
		else:
			GWK[_wk+cwait] -= 1
			if( GWK[_wk+cwait] < 0 ):
				GWK[_wk+ccond] |= F_LIVE

#-----------------------------------------------------------------
#ワープセット
#	開始（伸びるアニメ設定）
def star_warp_start():
	for _cnt in range(STARMAX):
		#手前側
		_wk = STAR1_WORK+(CHAR_MAX * _cnt)
		GWK[_wk+ccond] |= F_WARP
		GWK[_wk+canum] = 0x2a
		GWK[_wk+cacnt] = 0
		GWK[_wk+caspd] = 0
		#奥側
		_wk = STAR2_WORK+(CHAR_MAX * _cnt)
		GWK[_wk+ccond] |= F_WARP
		GWK[_wk+canum] = 0x2b
		GWK[_wk+cacnt] = 0
		GWK[_wk+caspd] = 0

#	終了（縮むアニメ設定）
def star_warp_end():
	for _cnt in range(STARMAX):
		#手前側
		_wk = STAR1_WORK+(CHAR_MAX * _cnt)
		GWK[_wk+ccond] |= F_WARPEND
		#GWK[_wk+caspd] = 0
		#奥側
		_wk = STAR2_WORK+(CHAR_MAX * _cnt)
		GWK[_wk+ccond] |= F_WARPEND
		#GWK[_wk+caspd] = 0

#-----------------------------------------------------------------
#星描画
def star_draw():
	for _cnt in range(STARMAX):
		#手前側
		_wk = STAR1_WORK+(CHAR_MAX * _cnt)
		if( GWK[_wk+ccond] & F_LIVE ):
			if( GWK[_wk+canum] != 0xff ):
				_id = atbl[GWK[_wk+canum]][GWK[_wk+cacnt]+1]
			else:
				_id = GWK[_wk+cid]
			_xp = GWK[_wk+cxpos]
			_yp = GWK[_wk+cypos]
			pyxel.blt( _xp, _yp, 0, ctbl[_id][0], ctbl[_id][1], ctbl[_id][2], ctbl[_id][3], 0 )
		
		#奥側
		_wk = STAR2_WORK+(CHAR_MAX * _cnt)
		if( GWK[_wk+ccond] & F_LIVE ):
			if( GWK[_wk+canum] != 0xff ):
				_id = atbl[GWK[_wk+canum]][GWK[_wk+cacnt]+1]
			else:
				_id = GWK[_wk+cid]
			_xp = GWK[_wk+cxpos]
			_yp = GWK[_wk+cypos]
			pyxel.blt( _xp, _yp, 0, ctbl[_id][0], ctbl[_id][1], ctbl[_id][2], ctbl[_id][3], 0 )

#-----------------------------------------------------------------
#敵
#	グループ単位でグループ内敵全員やられるまで次を出さない
#-----------------------------------------------------------------
#敵グループ１
#	動き番号
#		0:直進のみ
#		1,7:うねうね
#		2,8:ジグザグ
#		3,9:大まわり
#		4,d:プレイヤー方向へ移動（part2以降：破壊されたらショットON）
#		5,e:階段
#		6,f:下ではねかえり
#		a:下でプレイヤー方向へ
#		b:まっすぐ降りてきて一時停止、プレイヤー方向へ向かって斜め移動
#		c:プレイヤー方向へ向かって斜め高速移動
#
#
#		漂いながら３方向にSHOT（パワーアップ出すUFO赤）
#		左から出現、任意の位置で直進
#		右から出現、任意の位置で直進
#
#
#-----------------------------------------------------------------
#	敵グループ１生成（動き毎に設定が変更される）
def ene_g1_set():
	for _cnt in range(ENE_G1_MAX):
		_wk = ENE_G1_WORK+(CHAR_MAX * _cnt)
		GWK[_wk+cypos] = -30
		GWK[_wk+ccond] = F_ACTIVE
		GWK[_wk+cacnt] = 0
		GWK[_wk+caspd] = 0
		GWK[_wk+cid] = 0xff									#アニメ番号から指定するなら暫定
		GWK[_wk+cmnum] = _cnt								#グループ内移動パターン番号
		GWK[_wk+cmcnt] = 0									#移動カウンタ
		
		#動き番号で変化
		#うねうね（No.7はX位置ランダムのうねうね）
		#if( ( GWK[ene_g1_number] == 1 ) or ( GWK[ene_g1_number] == 7 ) ):
		if( GWK[ene_g1_number] == 1 ):
			GWK[_wk+canum] = 0x0e								#アニメ番号
			GWK[_wk+cwait] = _cnt*20							#登場待機時間時差長め
			GWK[_wk+cxpos] = int(SCREEN_WIDTH/2) - 8			#登場位置（中央）
			GWK[_wk+cxspd] = 0.0								#移動スピードx
			GWK[_wk+cyspd] = 2.0								#移動スピードy
		#ジグザグ（No.8はX位置ランダムのジグザグ）
		#elif( ( GWK[ene_g1_number] == 2 ) or ( GWK[ene_g1_number] == 8 ) ):
		elif( GWK[ene_g1_number] == 2 ):
			GWK[_wk+canum] = 0x0e								#アニメ番号
			GWK[_wk+cwait] = _cnt*20							#登場待機時間時差長め
			GWK[_wk+cxpos] = int(SCREEN_WIDTH/2) - 8			#登場位置（中央）
			GWK[_wk+cxspd] = 0.0								#移動スピードx
			GWK[_wk+cyspd] = 2.0								#移動スピードy
		#大まわり
		elif( ( GWK[ene_g1_number] == 3 ) or ( GWK[ene_g1_number] == 9 ) ):
			GWK[_wk+canum] = 0x16								#アニメ番号
			GWK[_wk+cwait] = _cnt*8								#登場待機時間時差短め
			GWK[_wk+cxpos] = int(SCREEN_WIDTH/2) - 8			#登場位置（中央）
			GWK[_wk+cxspd] = 0.0								#移動スピードx
			GWK[_wk+cyspd] = 2.0								#移動スピードy
		#プレイヤー方向へ移動（破壊されたらショットON）
		elif( ( GWK[ene_g1_number] == 4 ) or ( GWK[ene_g1_number] == 0x0d ) ):
			GWK[_wk+canum] = 0x1e								#アニメ番号
			GWK[_wk+cwait] = _cnt*20							#登場待機時間時差長め
			if(GWK[PLY_WORK+cxpos] > int(SCREEN_WIDTH/2) ):
				GWK[_wk+cxpos] = int(SCREEN_WIDTH * 1 / 4) - 20
			else:
				GWK[_wk+cxpos] = int(SCREEN_WIDTH * 3 / 4) + 20
			GWK[_wk+cxspd] = 0.0								#移動スピードx
			GWK[_wk+cyspd] = 2.0								#移動スピードy
		else:		#0
			GWK[_wk+canum] = 0x06								#アニメ番号
			GWK[_wk+cwait] = _cnt*20							#登場待機時間
			GWK[_wk+cxpos] = pyxel.rndi(0,SCREEN_WIDTH-0x10)	#登場位置
			GWK[_wk+cxspd] = 0.0								#移動スピードx
			GWK[_wk+cyspd] = 2.0								#移動スピードy

#-----------------------------------------------------------------
#	敵グループ１制御（出現管理と動き）
def ene_g1_control():
	for _cnt in range(ENE_G1_MAX):
		_wk = ENE_G1_WORK+(CHAR_MAX * _cnt)
		if(GWK[_wk+ccond] & F_LIVE):
			anim_control( _wk, 0 )
			#うねうね
			if( ( GWK[ene_g1_number] == 1 ) or ( GWK[ene_g1_number] == 7 ) ):
				_mvtbl1 = [-2,-2,-2,-2,-1,-1,-1,-1,0,0,0,0,1,1,1,1,2,2,2,2]
				_mvcnt = GWK[_wk+cmcnt]
				if( _mvcnt >= 20 ):
					_mvcnt -= 20
					_mvcnt = 19 - _mvcnt
				GWK[_wk+cxspd] = _mvtbl1[_mvcnt]
				GWK[_wk+cmcnt] += 1
				if( GWK[_wk+cmcnt] >= 40 ):
					GWK[_wk+cmcnt] -= 40
			#ジグザグ
			elif( ( GWK[ene_g1_number] == 2 ) or ( GWK[ene_g1_number] == 8 ) ):
				_mvtbl2 = [-4,-4,-4,-4,-3,-3,-3,-3,-2,-2,-2,-2,-1,-1,-1,-1,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
				_mvcnt = GWK[_wk+cmcnt]
				if( _mvcnt >= 36 ):
					_mvcnt -= 36
					_mvcnt = 35 - _mvcnt
				GWK[_wk+cxspd] = _mvtbl2[_mvcnt]
				GWK[_wk+cmcnt] += 1
				if( GWK[_wk+cmcnt] >= 72 ):
					GWK[_wk+cmcnt] -= 72
			#大まわり
			elif( ( GWK[ene_g1_number] == 3 ) or ( GWK[ene_g1_number] == 9 ) ):
				_mvtbl3 = [-8,-8,-8,-8,-8,-8,-4,-4,-4,-4,-4,-4,-2,-2,-2,-2,-2,-2,-1,-1,-1,-1,-1,-1,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,4,4,4,4,4,4,8,8,8,8,8,8]
				_mvcnt = GWK[_wk+cmcnt]
				if( _mvcnt >= 54 ):
					_mvcnt -= 54
					_mvcnt = 53 - _mvcnt
				GWK[_wk+cxspd] = _mvtbl3[_mvcnt]
				GWK[_wk+cmcnt] += 1
				if( GWK[_wk+cmcnt] >= 108 ):
					GWK[_wk+cmcnt] -= 108
			#プレイヤー方向へ移動（破壊されたらショットON）
			elif( ( GWK[ene_g1_number] == 4 ) or ( GWK[ene_g1_number] == 0x0d ) ):
				if( GWK[_wk+cmcnt] == 0 ):
					#プレイヤー方向取得
					_radian = pyxel.atan2(GWK[_wk+cypos] - GWK[PLY_WORK+cypos], GWK[_wk+cxpos] - GWK[PLY_WORK+cxpos] )
					#速度セット
					GWK[_wk+cyspd] = pyxel.sin(_radian) * (-3);
					GWK[_wk+cxspd] = pyxel.cos(_radian) * (-3);
					GWK[_wk+cmcnt] = 1
			#階段
			elif( ( GWK[ene_g1_number] == 5 ) or ( GWK[ene_g1_number] == 0x0e ) ):
				GWK[_wk+cmcnt]+=1
				if( GWK[_wk+cmcnt] >= 32 ):
					GWK[_wk+cmcnt] -= 32
					if(GWK[_wk+cxspd] == 0 ):
						GWK[_wk+cyspd] = 0
						if( GWK[_wk+cxpos] <= GWK[PLY_WORK+cxpos] ):
							GWK[_wk+cxspd] = 2
						else:
							GWK[_wk+cxspd] = -2
					else:
						GWK[_wk+cxspd] = 0
						GWK[_wk+cyspd] = 2
			#下ではねかえり
			elif( ( GWK[ene_g1_number] == 6 ) or ( GWK[ene_g1_number] == 0x0f ) ):
				if( GWK[_wk+cmcnt] == 0 ):	#下へ移動、プレイヤーY位置検索
					if(GWK[_wk+cypos] >= GWK[PLY_WORK+cypos]):
						if(GWK[_wk+cxpos] >= GWK[PLY_WORK+cxpos]):
							GWK[_wk+cxspd] = -2
						else:
							GWK[_wk+cxspd] = 2
						GWK[_wk+cmcnt] = 1
						GWK[_wk+cyspd] = -6
					else:
						GWK[_wk+cxspd] = 0
						GWK[_wk+cyspd] = 6
				elif( GWK[_wk+cmcnt] == 1 ):	#上へ移動、Y座標30%位置で下へ
					if(GWK[_wk+cypos] < int(SCREEN_HEIGHT * (3/10))):
						GWK[_wk+cxspd] = 0
						GWK[_wk+cyspd] = 4
						GWK[_wk+cmcnt] = 2
				else:
					GWK[_wk+cxspd] = 0
					GWK[_wk+cyspd] = 3
			#下でプレイヤー方向へ
			elif( GWK[ene_g1_number] == 0xa ):
				if( GWK[_wk+cmcnt] == 0 ):	#下へ移動、プレイヤーY位置検索
					if(GWK[_wk+cypos] >= GWK[PLY_WORK+cypos]):
						if(GWK[_wk+cxpos] >= GWK[PLY_WORK+cxpos]):
							GWK[_wk+cxspd]= -2
						else:
							GWK[_wk+cxspd] = 2

						GWK[_wk+cmcnt] = 1;
						GWK[_wk+cyspd] = 0;
					else:
						GWK[_wk+cxspd] = 0;
						GWK[_wk+cyspd] = 6;
				else:
					GWK[_wk+cyspd] = 0
			#まっすぐ降りてきて一時停止、プレイヤー方向へ向かって斜め移動
			elif( GWK[ene_g1_number] == 0xb ):
				if( GWK[_wk+cmcnt] == 0 ):
					GWK[_wk+cyspd] = 6
					GWK[_wk+cmcnt] = 1
					break;
				elif( GWK[_wk+cmcnt] == 1 ):
					if(GWK[_wk+cypos] > 50):
						GWK[_wk+cyspd] = 0
						GWK[_wk+cmcnt2] = 30
						GWK[_wk+cmcnt] = 2
				elif( GWK[_wk+cmcnt] == 2 ):
					GWK[_wk+cmcnt2] -= 1
					if(GWK[_wk+cmcnt2] < 0):
						#プレイヤー方向取得
						_radian = pyxel.atan2( GWK[_wk+cypos] - GWK[PLY_WORK+cypos], GWK[_wk+cxpos] - GWK[PLY_WORK+cxpos] );
						#速度セット
						GWK[_wk+cyspd] = pyxel.sin(_radian) * (-6);
						GWK[_wk+cxspd] = pyxel.cos(_radian) * (-6);
						GWK[_wk+cmcnt] = 3
				elif( GWK[_wk+cmcnt] == 3 ):
					pass
			#プレイヤー方向へ向かって斜め高速移動
			elif( GWK[ene_g1_number] == 0xc ):
				if( GWK[_wk+cmcnt] == 0 ):
					if(GWK[_wk+cxpos] >= GWK[PLY_WORK+cxpos]):
						GWK[_wk+cxspd] = -2
					else:
						GWK[_wk+cxspd] = 2
					GWK[_wk+cyspd] = 6
					GWK[_wk+cmcnt] = 1
					break;
				else:
					pass
			#直進
			else:	#0
				pass

			GWK[_wk+cxpos] += GWK[_wk+cxspd]
			if( GWK[_wk+cxpos] < ENE_XL_LIMIT ):
				GWK[_wk+ccond] = 0
				GWK[_wk+ccond] &= ~(F_LIVE+F_ACTIVE)
			if( GWK[_wk+cxpos] > ENE_XR_LIMIT ):
				GWK[_wk+ccond] = 0
				GWK[_wk+ccond] &= ~(F_LIVE+F_ACTIVE)
			GWK[_wk+cypos] += GWK[_wk+cyspd]
			if( GWK[_wk+cypos] > ENE_YD_LIMIT ):
				GWK[_wk+ccond] = 0
				GWK[_wk+ccond] &= ~(F_LIVE+F_ACTIVE)

		elif(GWK[_wk+ccond] & F_ACTIVE):
			#登場待ち
			GWK[_wk+cwait] -= 1
			if(GWK[_wk+cwait] < 0):
				GWK[_wk+cwait] = 0
				GWK[_wk+ccond] |= F_LIVE

#-----------------------------------------------------------------
#出現チェック
def ene_control():
	_cnt_g1 = 0
	for _cnt in range(ENE_G1_MAX):
		_wk = ENE_G1_WORK+(CHAR_MAX * _cnt)
		if(GWK[_wk+ccond] & (F_LIVE+F_ACTIVE)):
			_cnt_g1 += 1
	if( _cnt_g1 == 0 ):
		GWK[ene_g1_number] += 1
		if( GWK[ene_g1_number] > ENE_G1_MAX ):
			GWK[ene_g1_number] = 0
		ene_g1_set()

#-----------------------------------------------------------------
#	敵グループ１描画
def ene_g1_draw():
	for _cnt in range(ENE_G1_MAX):
		_wk = ENE_G1_WORK+(CHAR_MAX * _cnt)
		if(GWK[_wk+ccond] & F_LIVE):
			if( GWK[_wk+canum] != 0xff ):
				_id = atbl[GWK[_wk+canum]][GWK[_wk+cacnt]+1]
			else:
				_id = GWK[_wk+cid]
			_xp = GWK[_wk+cxpos]
			_yp = GWK[_wk+cypos]
			pyxel.blt( _xp, _yp, 0, ctbl[_id][0], ctbl[_id][1], ctbl[_id][2], ctbl[_id][3], 0 )

################################################################################
#制御
def game_control():
	#星制御
	star_control()
	ene_control()
	ene_g1_control()
	ptama_control()

	if getInputLEFT():
		GWK[PLY_WORK+cxpos] -= GWK[PLY_WORK+cxspd]
	if getInputRIGHT():
		GWK[PLY_WORK+cxpos] += GWK[PLY_WORK+cxspd]
	if getInputUP():
		GWK[PLY_WORK+cypos] -= GWK[PLY_WORK+cyspd]
	if getInputDOWN():
		GWK[PLY_WORK+cypos] += GWK[PLY_WORK+cyspd]

		if( GWK[PLY_WORK+cxpos] < PLY_XL_LIMIT ):
			GWK[PLY_WORK+cxpos] = PLY_XL_LIMIT
		if( GWK[PLY_WORK+cxpos] > PLY_XR_LIMIT ):
			GWK[PLY_WORK+cxpos] = PLY_XR_LIMIT
		if( GWK[PLY_WORK+cypos] < PLY_YU_LIMIT ):
			GWK[PLY_WORK+cypos] = PLY_YU_LIMIT
		if( GWK[PLY_WORK+cypos] > PLY_YD_LIMIT ):
			GWK[PLY_WORK+cypos] = PLY_YD_LIMIT


	if getInputA():
		#SHOT ON
		ptama_set()
	if getInputB():
		if( ( GWK[STAR1_WORK+ccond] & (F_WARP+F_WARPEND) ) == F_WARP ):
			star_warp_end()
		else:
			star_warp_start()

################################################################################
#描画
def game_draw():
	#星描画
	star_draw()
	ene_g1_draw()
	ptama_draw()

	#自機表示
	_id = GWK[PLY_WORK+cid]
	_xp = GWK[PLY_WORK+cxpos]
	_yp = GWK[PLY_WORK+cypos]
	pyxel.blt( _xp, _yp, 0, ctbl[_id][0], ctbl[_id][1], ctbl[_id][2], ctbl[_id][3], 0 )

#-----------------------------------------------------------------
#work clear
#-----------------------------------------------------------------
def work_clear():
	for _cnt in range( WORK_TOP, WORK_END ):
		GWK[_cnt] = 0

#-----------------------------------------------------------------
#入力（キーボード＆ジョイパッド）
#-----------------------------------------------------------------
#上
def getInputUP():
	if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
		return 1
	else:
		return 0
#下
def getInputDOWN():
	if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
		return 1
	else:
		return 0
#左
def getInputLEFT():
	if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
		return 1
	else:
		return 0
#右
def getInputRIGHT():
	if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
		return 1
	else:
		return 0
#button-A（決定）
def getInputA():
	if pyxel.btnp(pyxel.KEY_Z, hold=10, repeat=10) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A, hold=10, repeat=10):
		return 1
	else:
		return 0
#button-B（キャンセル）
def getInputB():
	if pyxel.btnp(pyxel.KEY_X) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
		return 1
	else:
		return 0
#button-X
def getInputX():
	if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):
		return 1
	else:
		return 0
#button-Y
def getInputY():
	if pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y):
		return 1
	else:
		return 0

#===============================================================================
#更新（main loop）
#===============================================================================
def update():
	#制御
	game_control()

#===============================================================================
#描画（demo:taku_disp()）
#===============================================================================
def draw():
	#画面クリア
	pyxel.cls(0)
	game_draw()

#===============================================================================
#INIT
#===============================================================================
#初期化から実行へ
pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=60)
#[use Web]ESCキーを無効化
#pyxel.init(256, 256, fps=60, quit_key=pyxel.KEY_NONE, title='pyxelsht')

#リソース読み込み
pyxel.load("pyxelsht.pyxres")

#BDFフォント読み込み
#bdf10 = BDFRenderer("font/umplus_j10r.bdf")
#bdf12 = BDFRenderer("font/umplus_j12r.bdf")

#ワーククリア
work_clear()

#初期値セット（仮）
GWK[PLY_WORK+cid] = 0x18
GWK[PLY_WORK+cxpos] = int( ( SCREEN_WIDTH - ctbl[GWK[PLY_WORK+cid]][2] ) / 2 )
GWK[PLY_WORK+cypos] = int( ( SCREEN_HEIGHT * 3 ) / 4 )
GWK[PLY_WORK+cxspd] = 2.0
GWK[PLY_WORK+cyspd] = 2.0

#各種初期化
star_init()
GWK[ene_g1_number] = 0
GWK[ene_g2_number] = 0
GWK[ene_g3_number] = 0

#仮敵出現
ene_g1_set()

#実行
pyxel.run(update, draw)
