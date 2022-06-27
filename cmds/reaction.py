from core.classes import Cog_Extension
import discord
import json
from discord_components import (
    DiscordComponents,
    Button,
    ButtonStyle,
    Select,
    SelectOption,
    Interaction,
)
import datetime
import asyncio
from discord.ext import commands
with open("set.json",'r',encoding='utf8')as jfile:
  jdata=json.load(jfile)





class reaction(Cog_Extension):
  @commands.command(name='大世界')
  async def 大世界(self,ctx):

    await ctx.send(
    "選擇敵艦名稱",
    components = [
    Select(

    placeholder = "敵艦名稱",
    options =[ (SelectOption(label = "代行者XIV[Equilibrium]", value = "XIV1")),
SelectOption(label = "代行者IX[Concealment]", value = "IX"),
SelectOption(label = "代行者VIII[Determination]", value = "VIII"),
SelectOption(label = "代行者IX[Exploration]", value = "IX1"),
SelectOption(label = "代行者XIV[Harmony]", value = "XIV")

                ]
            )
    ])
    aa= Select(

    placeholder = "文字說明",
    options =[ 
                    SelectOption(label = "特殊磁條", value = "F"),
                    SelectOption(label = "移動邏輯", value = "W"),
                    SelectOption(label = "攻略難點", value = "H")

                ]
            )
    bb= Select(

    placeholder = "文字說明",
    options =[ 
                    SelectOption(label = "特殊磁條", value = "F1"),
                    SelectOption(label = "移動邏輯", value = "W1"),
                    SelectOption(label = "攻略難點", value = "H1")

                ]
            )
    cc= Select(

    placeholder = "文字說明",
    options =[ 
                    SelectOption(label = "特殊磁條", value = "F2"),
                    SelectOption(label = "移動邏輯", value = "W2"),
                    SelectOption(label = "攻略難點", value = "H2")

                ]
            )
    dd= Select(

    placeholder = "文字說明",
    options =[ 
                    SelectOption(label = "特殊磁條", value = "F3"),
                    SelectOption(label = "移動邏輯", value = "W3"),
                    SelectOption(label = "攻略難點", value = "H3")

                ]
            )
    ee= Select(

    placeholder = "文字說明",
    options =[ 
                    SelectOption(label = "特殊磁條", value = "F4"),
                    SelectOption(label = "移動邏輯", value = "W4"),
                    SelectOption(label = "攻略難點", value = "H4")

                ]
            )
    try:
      while True:
        interaction=await self.bot.wait_for('select_option')
  
        
        if interaction.values[0]=='XIV1':
          embed1=discord.Embed(title="代行者XIV[Equilibrium]", color=0x000000,timestamp=datetime.datetime.now())
          embed1.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
          embed1.set_image(url='https://patchwiki.biligame.com/images/blhx/c/c7/nvfdxpaldwskp33vgpp65goit65xrsq.png')
          
          await interaction.respond(embed=embed1,components=[aa])

        elif interaction.values[0]=='F':
          embed=discord.Embed(title="特殊磁條", color=0xb0f2f1)
          embed.add_field(name="先鋒獵手", value="敵方旗艦對我方前排先鋒造成的傷害增加50%", inline=False)
          embed.add_field(name="盛大登場", value="敵方旗艦登場後，每過10秒提高自身全屬性提升10%，最高疊加5層", inline=False)
          embed.add_field(name="護盾：大量耐久", value="敵方旗艦會生成一個可以吸收自身最大耐久值20%的護盾，持續5秒", inline=False)
          embed.add_field(name="護盾：重點防禦", value="敵方旗艦會生成一個降低被暴擊概率100%的護盾，持續10秒", inline=False)
          embed.add_field(name="護盾：傷害偏轉", value="每隔20秒，敵方旗艦會生成一個將所有攻擊傷害轉變為1的護盾，護盾最多偏轉15次攻擊傷害，持續8秒", inline=False)
          embed.add_field(name="—————— 我是分隔線———————", value="​", inline=False)
          embed.add_field(name="防空強化", value="敵方旗艦的防空增加50%", inline=False)
          embed.add_field(name="—————— 我是分隔線———————", value="​", inline=False)
          embed.add_field(name="火力超載模塊", value="敵方旗艦耐久值下降至30%時，砲擊、雷擊上升100%，每場戰鬥僅會觸發一次。", inline=False)
          embed.add_field(name="裝甲超載模塊", value="敵方旗艦耐久值下降至30%時，有50%概率將受到的炮擊傷害降為1，每場戰鬥僅會觸發一次。", inline=False)
          embed.add_field(name="護盾超載模塊", value="敵方旗艦耐久值下降至30%時，生成一面能夠阻擋子彈的護盾，護盾永久存在。", inline=False)
          embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
          await interaction.respond(embed=embed,components=[aa])
        elif interaction.values[0]=='H':
          embed=discord.Embed(title="攻略難點", color=0xc2e4ff)
          embed.add_field(name="1.敵方42s時(受各人設備因素影響而延遲)會射出可鎖定黑幕彈幕,命中後我方視野被限制為直徑50,同時沉默後排武器。持續時間10s,黑幕彈幕反復命中可刷新時間,最晚一顆子彈最遲1s後命中(視我方位置決定)。", value="​", inline=False)
          embed.add_field(name="2.敵方45-56s移動邏輯為靠後默認移動軸,565-90s移動邏輯為靠前默認移動軸(切換邏輯後移動計時器刷新計數)", value="​", inline=False)
          embed.add_field(name="3.敵方58s時會釋放可鎖定聲吶型彈幕,隨後每間隔7.5s釋放一次,總共4次。命中後我方前排(包括潛艇)武器減45碼射程(鎖|定距離不變),且減速20%,持續5s。同時會釋放魚雷,出射時可視,三秒後隱形只留下尾跡。", value="​", inline=False)
          embed.add_field(name="4.敵方輸出模式多為魚雷,特殊武器激光則為全甲120%補正,重甲承傷(鋼板吾妻)十分劣勢。隊伍內最好搭配防雷拐,且保證|前排人手一件防魚雷隔艙。", value="​", inline=False)
          await interaction.respond(embed=embed,components=[aa])
        elif interaction.values[0]=='W':
          embed=discord.Embed(title="移動邏輯", color=0xa3f9ff)
          embed.add_field(name="00-04", value="進圖站樁", inline=False)
          embed.add_field(name="04-56", value="靠後默認移動軸", inline=False)
          embed.add_field(name="56-90", value="靠前默認移動軸", inline=False)
    
    
          await interaction.respond(embed=embed,components=[aa])

        
        
        
        elif interaction.values[0]=='IX':
          embed1=discord.Embed(title="代行者IX[Concealment]", color=0x000000,timestamp=datetime.datetime.now())
          embed1.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
          embed1.set_image(url='https://patchwiki.biligame.com/images/blhx/thumb/1/17/2ndcz4kqndkqee8845kj4c4igbbl91p.png/600px-%E5%A4%A7%E4%B8%96%E7%95%8C%E6%B7%B1%E6%B8%8A%E8%BD%BB%E5%B7%A1.png')
          await interaction.respond(embed=embed1,components=[bb])
          
          

        
    
    
        elif interaction.values[0]=='VIII':
          embed1=discord.Embed(title="代行者VIII[Determination]", color=0x000000,timestamp=datetime.datetime.now())

          embed1.set_image(url='https://patchwiki.biligame.com/images/blhx/thumb/2/21/4t8gih4t7dw9z778hzzjisnldgp8iy6.png/600px-%E5%A4%A7%E4%B8%96%E7%95%8C%E6%B7%B1%E6%B8%8A%E9%87%8D%E5%B7%A1.png')
          await interaction.respond(embed=embed1,components=[cc])
        elif interaction.values[0]=='IX1':
          embed1=discord.Embed(title="代行者IX[Exploration]", color=0x000000,timestamp=datetime.datetime.now())
          embed1.set_image(url='https://patchwiki.biligame.com/images/blhx/thumb/d/de/rrksx5xbr7xgn9sz2zf5ox5i1vc6nw3.png/1024px-%E5%A4%A7%E4%B8%96%E7%95%8C%E6%B7%B1%E6%B8%8A%E6%88%98%E5%88%97.png')
          
          await interaction.respond(embed=embed1,components=[dd])
        elif interaction.values[0]=='XIV':
          embed1=discord.Embed(title="代行者XIV[Harmony]", color=0x000000,timestamp=datetime.datetime.now())
          embed1.set_image(url='https://patchwiki.biligame.com/images/blhx/thumb/d/d2/scqr4jklbaxfq4pkf2hjjuduo4q4kpi.png/1024px-%E5%A4%A7%E4%B8%96%E7%95%8C%E6%B7%B1%E6%B8%8A%E8%88%AA%E6%AF%8D.png')
          
          await interaction.respond(embed=embed1,components=[ee])
        elif interaction.values[0]=='F1':
          embed=discord.Embed(title="特殊磁條", color=0xb4f3f2)
          embed.add_field(name="航速強化", value="敵方旗艦的航速增加30%", inline=False)
          embed.add_field(name="—————— 我是分隔線———————", value="​", inline=False)
          embed.add_field(name="盛大登場", value="敵方旗艦登場後,每過10秒提高自身全屬性提升10%,最高疊加5層", inline=False)
          embed.add_field(name="先鋒獵手", value="敵方旗艦對我方前排先鋒造成的傷害增加50%", inline=False)
          embed.add_field(name="護盾：大量耐久", value="敵方旗艦會生成一個可以吸收自身最大耐久值20%傷害的護盾,持續5秒", inline=False)
          embed.add_field(name="護盾：重點防禦", value="每隔20秒,敵方旗艦會生成一個降低被暴擊概率100%的護盾,持續10秒", inline=False)
          embed.add_field(name="護盾：傷害偏轉", value="每隔20秒,敵方旗艦會生成一個將所受攻擊傷害變為1的護盾,護盾最多偏轉15次攻擊傷害,持續8秒", inline=False)
          embed.add_field(name="恢復轉移", value="敵方旗艦在場時,針對我方角色的恢復效果將會全部轉移至敵方旗艦上", inline=False)
          embed.add_field(name="—————— 我是分隔線———————", value="​", inline=False)
          embed.add_field(name="火力超載模塊", value="敵方旗艦耐久值下降至30%以下時,砲擊,雷擊上升100%,每場戰鬥僅會觸發一次", inline=False)
          embed.add_field(name="維修超載模塊", value="敵方旗艦耐久值下降至30%以下時,每隔3秒回復自身最大耐久值的5%,持續15秒,每場戰鬥僅會觸發一次", inline=False)
          embed.add_field(name="護盾超載模塊", value="敵方旗艦耐久值下降至30%以下時,生成一面能夠阻擋子彈的護盾,護盾永久存在", inline=False)
  
          embed.set_footer(text="資料來源：碧藍航線WIKI_碧藍海事局")
          await interaction.respond(embed=embed,components=[bb])
        elif interaction.values[0]=='F2':
          embed=discord.Embed(title="特殊磁條", color=0xadfffe)
          embed.add_field(name="砲擊強化", value="敵方旗艦的砲擊增加50%", inline=False)
          embed.add_field(name="—————— 我是分隔線———————", value="​", inline=False)
          embed.add_field(name="先鋒獵手", value="敵方旗艦對我方前排先鋒造成的傷害增加50%", inline=False)
          embed.add_field(name="盛大登場", value="敵方旗艦登場後,每過1自身全屬性提升10%,最高疊加5層", inline=False)
          embed.add_field(name="護盾:重點防禦", value="每隔20秒,敵方旗艦會生成一個降低被暴擊概率100%的護盾,持續10秒", inline=False)
          embed.add_field(name="護盾:傷害偏轉", value="每隔20秒,敵方旗艦會生成一個將所受攻擊傷害變為1的護盾,護盾最多偏轉15次攻擊傷害,持續8秒", inline=False)
          embed.add_field(name="恢復反轉", value="敵方旗艦在場時,我方全部角色受到的恢復效果會被反轉為傷害效果", inline=False)
          embed.add_field(name="—————— 我是分隔線———————", value="​", inline=False)
          embed.add_field(name="火力超載模塊", value="敵方旗艦耐久值下降至30%以下時,砲擊、雷擊上升100%,每場戰鬥僅會觸發一次", inline=False)
          embed.add_field(name="裝甲超載模塊", value="敵方旗艦耐久值下降至30%以下時,有50%概率將受到的砲擊傷害降為1,每場戰鬥僅會觸發一次", inline=False)
          embed.add_field(name="護盾超載模塊", value="敵方旗艦耐久值下降至30%以下時,生成一面能夠阻擋子彈的護盾,護盾永久存在", inline=False)
          await interaction.respond(embed=embed,components=[cc])

        elif interaction.values[0]=='F3':  
          embed=discord.Embed(title="特殊磁條")
          embed.add_field(name="砲擊強化", value="敵方旗艦的砲擊增加50%", inline=False)
          embed.add_field(name="—————— 我是分隔線———————", value="​", inline=False)
          embed.add_field(name="獵手", value="敵方旗艦對我方所有角色造成的傷害增加30%", inline=False)
          embed.add_field(name="先鋒獵手", value="敵方旗艦對我方前排先鋒造成的傷害增加50%", inline=False)
          embed.add_field(name="主力獵手", value="敵方旗艦對我方後排主力造成的傷害增加50%", inline=False)
          embed.add_field(name="毀滅", value="敵方旗艦登場後,每過10秒對我方全體角色造成最大耐久值5%的傷害", inline=False)
          embed.add_field(name="盛大登場", value="敵方旗艦登場後,每過10秒提高自身全屬性提升10%,最高疊加5層", inline=False)
          embed.add_field(name="恢復轉移", value="敵方旗艦在場時,針對我方角色的恢復效果將會全部轉移至敵方旗艦上", inline=False)
          embed.add_field(name="—————— 我是分隔線———————", value="​", inline=False)
          embed.add_field(name="火力超載模塊", value="敵方旗艦耐久值下降至30%以下時,砲擊、雷擊上升100%,每場戰鬥僅會觸發一次", inline=False)
          embed.add_field(name="裝甲超載模塊", value="敵方旗艦耐久值下降至30%以下時,有50%概率將受到的砲擊傷害降為1,每場戰鬥僅會觸發一次", inline=False)
          embed.add_field(name="維修超載模塊", value="敵方旗艦耐久值下降至30%以下時,每隔3秒回復自身最大耐久值的5%,持續15秒,每場戰鬥僅會觸發一次", inline=False)

          await interaction.respond(embed=embed,components=[dd])
        elif interaction.values[0]=='F4':  
          embed=discord.Embed(title="特殊磁條")
          embed.add_field(name="航空強化", value="敵方旗艦的航空增加50%", inline=False)
          embed.add_field(name="—————— 我是分隔線———————", value="​", inline=False)
          embed.add_field(name="毀滅", value="敵方旗艦登場後,每過10秒對我方全體角色造成最大耐久值5%的傷害", inline=False)
          embed.add_field(name="盛大登場", value="敵方旗艦登場後,每過10秒提高自身全屬性提升10%,最高疊加5層", inline=False)
          embed.add_field(name="護盾：大量耐久", value="敵方旗艦會生成一個可以吸收自身最大耐久值20%傷害的護盾,持續5秒", inline=False)
          embed.add_field(name="護盾：傷害偏轉", value="每隔20秒,敵方旗艦會生成一個將所受攻擊傷害變為1的護盾,護盾最多偏轉15次攻擊傷害,持續8秒", inline=False)
          embed.add_field(name="—————— 我是分隔線———————", value="​", inline=False)
          embed.add_field(name="火力超載模塊", value="敵方旗艦耐久值下降至30%以下時,砲擊、雷擊上升100%,每場戰鬥僅會觸發一次", inline=False)
          embed.add_field(name="裝甲超載模塊", value="敵方旗艦耐久值下降至30%以下時,有50%概率將受到的砲擊傷害降為1,每場戰鬥僅會觸發一次", inline=False)
          embed.add_field(name="維修超載模塊", value="敵方旗艦耐久值下降至30%以下時,每隔3秒回復自身最大耐久值的5%,持續15秒,每場戰鬥僅會觸發一次", inline=False)

          await interaction.respond(embed=embed,components=[ee])
        elif interaction.values[0]=='H1':
          embed=discord.Embed(title="攻略難點")
          embed.add_field(name="1.敵方在22s時會鋪下一片粉色煙幕,在煙霧中的我方單位會受到30%減速debuff,20%減命中debuff,以及受到最大生命百分比的點燃傷害,同時瞬移到我方先鋒艦隊固定的相對位置處,隨後扔下兩輪雷,每輪四顆,延遲1s。在此之後會站樁大約4s。由於我方位置隨機,且我方後排射程為50-200,此時有概率會瞬移出我方後排戰列的射程之外,導致無法鎖定開砲,但是會進|入戰列副砲射程。攻略時可酌情攜帶B-13或者凱旋炮。", value="​", inline=False)
          embed.add_field(name="2.敵方在70s生成第二輪粉色煙幕,隨後瞬移到我方艦隊固定的相對位置處,扔三輪雷每輪五顆,延遲0.6s,在此之後會在原地站|樁大約10s然後繼續移動。", value="​", inline=False)
          embed.add_field(name="3.敵方輸出模式多為魚雷,重甲承傷(鋼板吾妻)十分劣勢。隊伍內最好搭配防雷拐,且保證前排人手一件防魚雷隔艙。", value="​", inline=False)
  
          await interaction.respond(embed=embed,components=[bb])
        elif interaction.values[0]=='H2':  
          embed=discord.Embed(title="攻略難點")
          embed.add_field(name="1.在5s時直射一顆光彈,沿途留下三個引力場,持續155,範圍14碼。藍色引力場內(超重),我方先鋒航速降低50%,且射程降低35碼(不影響索敵),但增加10固定傷害,綠色引力場內(失),我方先鋒航速提高100%(會觸碰到80%的提速上限),且射程提高15碼(不影響索敵),但減少12固定傷害,同時處於兩個引力場則移速取先生效數值,射程取後生效數值,固定傷害部分疊加。", value="在225時散射四枚砲彈,分別落在我方移動範圍的四個角落,並在落點生成引力場,持續15s,範圍14碼,左上右下為綠色引力場,左下右上為藍色引力場,效果與上一條相同", inline=False)
          embed.add_field(name="2.若進入進攻形態,鍊式子母彈為藍白色,45s時會生成一個巨型引力場,範圍125碼,將我方前排向其吸引過去,引力大小為4.效果為對我方艦船指向敵人方向添加一個速度向量,大小為4/d(碼/幀),d為敵我間距;若進入防禦形態,鍊式子母彈為藍黑色,45s時會生成一個能抵擋12w傷害的AT力場,最多存在40s,被擊破時生成兩道弧形羽毛彈幕。移動邏輯", value="​", inline=False)
          await interaction.respond(embed=embed,components=[cc])
        elif interaction.values[0]=='H3':  
          embed=discord.Embed(title="攻略難點")
          embed.add_field(name="1.7s-20s有三輪針對前排的跨射,28%概率附帶藍火灼燒的點燃效果,持續12s,1s跳一次,標傷28,係數0.4。", value="​", inline=False)
          embed.add_field(name="2.第一段跨射:25s開始蓄力(期間對其造成2.8w傷害可打斷蓄力),30s時射出五輪高爆彈,每輪延遲1s,80%概率附帶藍火灼燒的點燃效果,持續12s,1s跳一次,係數0.4。前兩輪五顆,後三輪七顆(最兩側各多一顆)。傷害範圍15,落點間距15(散的非常開)。|補正110%80%70%,標傷60。", value="​", inline=False)
          embed.add_field(name="3.第二段跨射:39s開始蓄力(期間對其造成3.2w傷害可打斷蓄力),44s時射出一連串17顆紫色+19顆藍色(藍色較為集中看起來會|比較少)穿甲跨射,整個過程持續3s。紫色子彈在z方向32長度內散佈,藍色子彈在z方向16範圍散佈。補正50%110%120%(紫色),50%110%125(藍色)", value="​", inline=False)
          embed.add_field(name="4.第三段跨射:53s開始蓄力(期間對其造成3.6w傷害可打斷蓄力),58s時射出五輪高爆彈,與第一段跨射完全相同。", value="​", inline=False)
          embed.add_field(name="5. 54s時開始激光預警,5s後交叉射出藍色冰霧激光,隨後逐漸向外旋轉,持續6s。全甲補正120%", value="​", inline=False)
          embed.add_field(name="6. 77.5s時開始蓄力,5s後釋放11顆流星雨,每顆間隔2.5s。全甲補正120%。範圍較小,很容易躲開。", value="​", inline=False)
          await interaction.respond(embed=embed,components=[dd])
        elif interaction.values[0]=='H4':  
          embed=discord.Embed(title="攻略難點")
          embed.add_field(name="1.4s時釋放菱形曳光彈,圓形向外輻射。標傷24,補正60%,80%,100%。同時釋放藍色光點彈幕,標傷24,補正100%,80%,60%。", value="​", inline=False)
          embed.add_field(name="2.18s時釋放淺藍色熒光子彈,中心放射狀,標傷24,補正60%,80%,100%。", value="​", inline=False)
          embed.add_field(name="3.19s時釋放六架浮游炮,每架浮游炮攜帶紫色彈藥,鎖定攻擊,標傷19,補正100%,90%,60%。", value="​", inline=False)
          embed.add_field(name="4.41s時釋放18個母彈圍繞一圈,傷害28,補正100%,70%,30%,並旋轉釋放藍色熒光子彈,傷害16,補正60%,80%,100%。砲擊", value="​", inline=False)
          embed.add_field(name="5.釋放高速魚雷機,86標傷,補正80%,100%,130%,前置浮游炮藍色彈幕,標傷19,補正100%,80%,40%。", value="​", inline=False)
          embed.add_field(name="6.53s由母彈釋放藍色熒光螺旋狙擊彈幕,標傷12,補正60%,80%,100%,重複8次,間隔4.8s", value="​", inline=False)
          embed.add_field(name="7. 74s由母彈釋放兩種藍色熒光彈幕,標傷12,補正均為60%,80%,100%,重複兩輪。", value="​", inline=False)
          embed.add_field(name="8.13s、50s、86s釋放桃花彈幕,標傷4,補正100%,70%,30%。除第4條外,所有彈幕均為航空加成。", value="​", inline=False)
          await interaction.respond(embed=embed,components=[ee])
          
        elif interaction.values[0]=='W1':
          embed=discord.Embed(title="移動邏輯")
          embed.add_field(name="00-04", value="進圖站樁", inline=False)
          embed.add_field(name="04-12", value="默認移動軸", inline=False)
          embed.add_field(name="12-22", value="靠後默認移動軸", inline=False)
          embed.add_field(name="22-26", value="投雷並站樁", inline=False)
          embed.add_field(name="26-47", value="默認移動軸", inline=False)
          embed.add_field(name="47-71", value="默認移動軸", inline=False)
          embed.add_field(name="71-81", value="投雷並站樁", inline=False)
          embed.add_field(name="81-90", value="靠後默認移動軸", inline=False)
    
          await interaction.respond(embed=embed,components=[bb])
        elif interaction.values[0]=='W2':
          embed=discord.Embed(title="移動邏輯")
          embed.add_field(name="04-37", value="默認移動軸", inline=False)
          embed.add_field(name="37-44", value="前往座標(0,57)站樁，右側版邊", inline=False)
          embed.add_field(name="在42-44內判定", value="如果 血量高於40%(進入攻擊型態)，則靠後默認移動軸，運動到結束\n如果血量高於40%(進入防禦狀態)，則原地站樁到結束", inline=False)
          await interaction.respond(embed=embed,components=[cc])
        elif interaction.values[0]=='W3':
          embed=discord.Embed(title="移動邏輯")
          embed.add_field(name="00-04", value="進圖站樁", inline=False)
          embed.add_field(name="04-68", value="靠後默認移動軸", inline=False)
          embed.add_field(name="68-77.5", value="靠前默認移動軸", inline=False)
          embed.add_field(name="77.5-90", value="默認移動軸", inline=False)
          await interaction.respond(embed=embed,components=[dd])
        elif interaction.values[0]=='W4':
          embed=discord.Embed(title="移動邏輯")
          embed.add_field(name="00-04", value="進圖發呆", inline=False)
          embed.add_field(name="04-90", value="默認移動軸", inline=False)
          await interaction.respond(embed=embed,components=[ee])
     
        
    

    except asyncio.TimeoutError:
      pass
   
    

def setup(bot):
  bot.add_cog(reaction(bot))