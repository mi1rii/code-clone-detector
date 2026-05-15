def text(ctx, string, pos, theta = 0.0, face = 'Georgia', font_size = 18) :
	ctx.save()
	ctx.select_font_face(face, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
	ctx.set_font_size(font_size)
	fascent, fdescent, fheight, fxadvance, fyadvance = ctx.font_extents()
	x_off, y_off, tw, th = ctx.text_extents(string) [: 4]
	nx = - tw / 2.0
	ny = fheight / 2
	ctx.translate(pos [0], pos [1])
	ctx.rotate(theta)
	ctx.translate(nx, ny)
	ctx.move_to(0, 0)
	ctx.show_text(string)
	ctx.restore()


def var_1(var_2, var_3, var_4, var_5 = 0.0, var_6 = 'Georgia', var_7 = 18) :
	var_2.var_8()
	var_2.var_9(var_6, var_10.var_11, var_10.var_12)
	var_2.var_13(var_7)
	var_14, var_15, var_16, var_17, var_18 = var_2.var_19()
	var_20, var_21, var_22, var_23 = var_2.var_24(var_3) [: 4]
	var_25 = - var_22 / 2.0
	var_26 = var_16 / 2
	var_2.var_27(var_4 [0], var_4 [1])
	var_2.var_28(var_5)
	var_2.var_27(var_25, var_26)
	var_2.var_29(0, 0)
	var_2.var_30(var_3)
	var_2.var_31()
