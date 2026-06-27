import base64, pathlib

with open(r'C:\Users\User\Downloads\Myke_Agent\Dentstage凹痕工廠相關事項\Dent Stage LOGO 圓 更新.png','rb') as f:
    LOGO = 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

HTML = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Dentstage 凹痕工廠 — 會議紀錄 2026.06.22</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:"Microsoft JhengHei","PingFang TC",sans-serif;background:#f4f4f4;color:#222;padding:32px 16px}}
.page{{max-width:900px;margin:0 auto;background:#fff;border-radius:8px;box-shadow:0 4px 24px rgba(0,0,0,.1);overflow:hidden}}
.header{{background:#1a1a1a;padding:28px 44px;display:flex;align-items:center;gap:24px}}
.header img{{width:80px;height:80px;border-radius:50%;object-fit:cover;flex-shrink:0}}
.header-text h1{{font-size:20px;font-weight:800;color:#fff;letter-spacing:2px}}
.header-text h2{{font-size:13px;color:#bbb;margin-top:5px}}
.header-badge{{margin-left:auto;text-align:right}}
.header-badge .date{{font-size:26px;font-weight:700;color:#c0392b;line-height:1}}
.header-badge .label{{font-size:10px;color:#888;margin-top:3px;letter-spacing:1px}}
.meta-bar{{background:#c0392b;padding:10px 44px;display:flex;gap:36px;flex-wrap:wrap}}
.meta-item{{color:#fff;font-size:12.5px}}
.meta-item span{{font-weight:600;opacity:.8}}
.body{{padding:36px 44px}}
.section{{margin-bottom:32px}}
.section-title{{display:flex;align-items:center;gap:10px;margin-bottom:14px;padding-bottom:6px;border-bottom:2px solid #c0392b}}
.num{{background:#c0392b;color:#fff;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;flex-shrink:0}}
.section-title h3{{font-size:15px;font-weight:700}}
table{{width:100%;border-collapse:collapse;font-size:13px;margin-top:6px}}
th{{background:#1a1a1a;color:#fff;padding:9px 13px;text-align:left;font-weight:600}}
td{{padding:8px 13px;border-bottom:1px solid #eee;vertical-align:top;line-height:1.65}}
tr:nth-child(even) td{{background:#f9f9f9}}
.sub{{font-size:13px;font-weight:600;color:#1a1a1a;margin:14px 0 6px}}
ul{{list-style:none}}
ul li{{padding:5px 0 5px 18px;position:relative;font-size:13.5px;line-height:1.7;border-bottom:1px solid #f0f0f0}}
ul li::before{{content:"▸";color:#c0392b;position:absolute;left:0;font-size:11px;top:7px}}
ul li:last-child{{border-bottom:none}}
.note{{background:#fff8f8;border-left:4px solid #c0392b;padding:12px 16px;margin:10px 0;font-size:13px;line-height:1.8;border-radius:0 4px 4px 0}}
.note strong{{color:#c0392b}}
.flow{{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin:10px 0}}
.step{{background:#1a1a1a;color:#fff;padding:5px 12px;border-radius:4px;font-size:12.5px;font-weight:600}}
.arr{{color:#c0392b;font-size:16px;font-weight:700}}
.footer{{background:#1a1a1a;padding:16px 44px;display:flex;justify-content:space-between;align-items:center}}
.footer p{{font-size:11px;color:#888}}
@media(max-width:600px){{.body{{padding:24px 18px}}.header{{padding:20px 18px}}.meta-bar{{padding:10px 18px;gap:16px}}}}
@media print{{body{{background:#fff;padding:0}}.page{{box-shadow:none;border-radius:0}}}}
</style>
</head>
<body>
<div class="page">

<div class="header">
  <img src="{LOGO}" alt="Dentstage">
  <div class="header-text">
    <h1>DENTSTAGE 凹痕工廠</h1>
    <h2>部門工作分配與業務流程規劃會議</h2>
  </div>
  <div class="header-badge">
    <div class="date">2026.06.22</div>
    <div class="label">MEETING MINUTES</div>
  </div>
</div>

<div class="meta-bar">
  <div class="meta-item"><span>主持：</span>Jay</div>
  <div class="meta-item"><span>出席：</span>Jay、Mary</div>
  <div class="meta-item"><span>地點：</span>Dentstage 凹痕工廠</div>
  <div class="meta-item"><span>性質：</span>內部工作分配會議</div>
</div>

<div class="body">

<!-- 1 人員職責分工 -->
<div class="section">
  <div class="section-title"><div class="num">1</div><h3>人員職責分工</h3></div>
  <table>
    <tr><th>工作項目</th><th>負責人</th><th>備註</th></tr>
    <tr><td>KECO 採購（下單、帳號管理）</td><td>Jay</td><td>Jay 提供各供應商網站帳號密碼給採購同仁</td></tr>
    <tr><td>進貨驗收 / 倉管</td><td>主任</td><td>8/1 入職後接手；Mary 採購完先 key 採購單，主任對單驗收</td></tr>
    <tr><td>出貨 / 銷貨</td><td>主任</td><td>不在時由 Mary cover</td></tr>
    <tr><td>庫存扣帳（實體倉）</td><td>主任</td><td>出貨後執行；網站庫存由系統自動扣</td></tr>
    <tr><td>報價單出單</td><td>Mary ＋ 主任</td><td>鼎新上負責人欄位須填本人姓名，不得出現對方名字</td></tr>
    <tr><td>網站上架 / 下架</td><td>Mary</td><td>電腦操作由 Mary 負責</td></tr>
    <tr><td>網站庫存扣帳</td><td>主任</td><td>非網站訂單的手動扣帳由主任執行</td></tr>
    <tr><td>FB / IG 貼文</td><td>Mary</td><td></td></tr>
    <tr><td>客訴 / 換貨 / 瑕疵品</td><td>Mary（主力）</td><td>國外窗口由 Mary 負責；大陸客戶由主任配合</td></tr>
    <tr><td>外訪廠商 / 學校</td><td>主任</td><td>主任外出時由 Jay 代理</td></tr>
  </table>
  <div class="note"><strong>主任到職日：2026 年 8 月 1 日</strong>，入職第一週先執行盤點，熟悉倉庫與系統後正式接手出貨、進貨、倉管工作。</div>
</div>

<!-- 2 採購供應商 -->
<div class="section">
  <div class="section-title"><div class="num">2</div><h3>採購供應商窗口整理</h3></div>
  <table>
    <tr><th>供應商</th><th>下單方式</th><th>付款 / 備註</th></tr>
    <tr><td>KECO</td><td>網站下單（Jay 提供帳號密碼）</td><td>天篷（Kimi）付款</td></tr>
    <tr><td>VIP</td><td>FB 群組 / 微信群（Jay 已建群）</td><td>很久未購入，重新聯繫中</td></tr>
    <tr><td>Ultra</td><td>供應商直接下單 → 寄台灣</td><td>多品項需下架（已被取代）；大量品項待下價</td></tr>
    <tr><td>Anson</td><td>窗口 Lisa（待確認聯繫方式）</td><td></td></tr>
    <tr><td>Blehm</td><td>網站下單</td><td>可寄至 Ultra 倉轉運；8～9 折優惠，Jay 尚未聯繫，待銜接</td></tr>
    <tr><td>PDR Finesse</td><td>KECO / Dencraft 網站順便購買</td><td>無折扣；Dencraft 僅少量折扣</td></tr>
    <tr><td>Dencraft</td><td>網站下單</td><td>頭（tips）需從網站購買；桿子另外談</td></tr>
    <tr><td>Black Plague</td><td>Email 窗口（待補充）</td><td></td></tr>
    <tr><td>Stanliner</td><td>暫不開放</td><td>每項商品較特殊，待 Jay 直接處理</td></tr>
    <tr><td>自製品（金剛、喬聖亞、光板等）</td><td>由 Mary 聯絡廠商</td><td>Kenji 訂製光板退款事宜（每片 20–30 RMB）待確認</td></tr>
    <tr><td>Amazon（錘子）</td><td>透過 Sally 詢價</td><td>見第 6 節討論事項</td></tr>
  </table>
</div>

<!-- 3 銷貨流程 -->
<div class="section">
  <div class="section-title"><div class="num">3</div><h3>銷貨流程規範</h3></div>
  <div class="note"><strong>核心原則：收到款項即銷貨（不等出貨）</strong></div>
  <div class="sub">■ 一般散客（網路下單 / 刷卡 / 匯款）</div>
  <div class="flow">
    <div class="step">客戶下單付款</div><div class="arr">→</div>
    <div class="step">確認收款</div><div class="arr">→</div>
    <div class="step">銷貨</div><div class="arr">→</div>
    <div class="step">出貨</div>
  </div>
  <div class="sub">■ 特殊情況：先出貨、後收款（學校 / 公司行號）</div>
  <div class="flow">
    <div class="step">確認訂單</div><div class="arr">→</div>
    <div class="step">出貨</div><div class="arr">→</div>
    <div class="step">銷貨</div><div class="arr">→</div>
    <div class="step">進入代結帳區</div><div class="arr">→</div>
    <div class="step">確認收款後結清</div>
  </div>
  <p style="font-size:12.5px;color:#666;margin-top:6px">「代結帳區」由主任管控，包含：客戶名稱、金額、已結/未結狀態，與 Jay / 天篷（Kimi）共用雲端表格。</p>
  <div class="sub">■ 帳款結算方式</div>
  <ul>
    <li>一般帳款（台幣）：直接與天篷（Kimi）結算</li>
    <li>主任月帳：與天篷（Kimi）結算</li>
    <li>人民幣帳款：與 Jay 結算（使用 Jay 帳戶）</li>
    <li>現場預備金：NT$30,000（由天篷（Kimi）每月補回）</li>
  </ul>
</div>

<!-- 4 大陸業務 -->
<div class="section">
  <div class="section-title"><div class="num">4</div><h3>大陸業務對接</h3></div>
  <table>
    <tr><th>項目</th><th>負責人</th><th>說明</th></tr>
    <tr><td>嫂子（大陸代理）日常對接</td><td>主任</td><td>原由 Mary 處理，8/1 後移交主任；嫂子尚未知情</td></tr>
    <tr><td>微信客服窗口</td><td>主任</td><td>使用公司手機；微信名稱建議改為「DentStage 張[主任姓名]」</td></tr>
    <tr><td>大陸客戶網站下單</td><td>Mary</td><td>Mary 確認後通知主任出貨</td></tr>
    <tr><td>大陸倉庫存管理</td><td>主任</td><td>移倉已完成；主任負責盤點與出貨給嫂子</td></tr>
    <tr><td>大陸倉售價制定</td><td>主任</td><td>主任負責管控成本與利潤，可調整售價</td></tr>
    <tr><td>WhatsApp / 其他國際客戶</td><td>Mary</td><td>非大陸地區國際客戶統一由 Mary 處理</td></tr>
  </table>
</div>

<!-- 5 盤點 -->
<div class="section">
  <div class="section-title"><div class="num">5</div><h3>盤點計畫</h3></div>
  <ul>
    <li>主任入職後第一週執行全倉盤點，作為熟悉倉庫與系統的實作訓練</li>
    <li>盤點範圍：鼎新大陸倉倉別清單（Mary 已移入完畢，數量最完整）</li>
    <li>盤點前需確認中間進銷貨異動，避免數量差異</li>
    <li>盤點完成後才可正式提供嫂子（大陸倉）庫存數量</li>
    <li>設定半年一次定期盤點制度</li>
  </ul>
  <div class="note" style="margin-top:10px"><strong>⚠</strong> 目前倉庫已部分盤點，移倉後有品項未即時銷貨扣帳，建議主任入職後<strong>優先清帳</strong>，避免庫存落差持續擴大。</div>
</div>

<!-- 6 其他討論 -->
<div class="section">
  <div class="section-title"><div class="num">6</div><h3>其他討論事項</h3></div>
  <div class="sub">■ 錘子採購評估（Amazon / Sally）</div>
  <ul>
    <li>Sally 詢價結果：100 支 × US$38.5 / 支，折扣後約 US$3,080（約 NT$98,560 + 運費）</li>
    <li>建議零售定價 NT$360 / 支；給大陸批發客九折（NT$324）</li>
    <li>毛利約 10%，但可預收款項再出貨，無庫存風險</li>
    <li>待辦：與大陸嫂子確認是否接受九折 NT$324 / 支，確認後再決定是否下單</li>
  </ul>
  <div class="sub">■ 網站二手工具欄位</div>
  <ul>
    <li>網站目前欄位已滿（WooCommerce / WarpLayers 限制）</li>
    <li>決議：將「設備」欄位併入「配件」，「收縮機」改標記為配件類</li>
    <li>待辦：通知大砲（網站管理員）執行合併，空出欄位給「二手工具」</li>
  </ul>
  <div class="sub">■ Pillon 膠水補貨</div>
  <ul>
    <li>已下訂 20 包 × 1kg，等待 Bruna 回覆中，若無回應再催促</li>
  </ul>
  <div class="sub">■ 工作效率（內部提醒）</div>
  <ul>
    <li>早餐訂購、分餐等非職責工作應委由店長安排，避免佔用正式上班時間</li>
    <li>後續代辦統一管理午餐訂購</li>
  </ul>
</div>

<!-- 7 Action Items -->
<div class="section">
  <div class="section-title"><div class="num">7</div><h3>行動清單 Action Items</h3></div>
  <table>
    <tr><th>待辦事項</th><th>負責人</th><th>期限 / 狀態</th></tr>
    <tr><td>提供 KECO 網站帳號密碼給採購同仁</td><td>Jay</td><td>待辦</td></tr>
    <tr><td>VIP / Black Plague / Anson 窗口資料補充</td><td>Jay</td><td>待辦</td></tr>
    <tr><td>與大陸確認錘子九折報價（NT$324/支）</td><td>Mary</td><td>待辦</td></tr>
    <tr><td>催促 Pillon 膠水訂單（聯絡人 Bruna）</td><td>Jay</td><td>待辦</td></tr>
    <tr><td>通知大砲合併「設備」至「配件」欄位</td><td>Mary</td><td>待辦</td></tr>
    <tr><td>Kenji 光板退款金額確認（20–30 RMB/片）</td><td>Mary</td><td>待辦</td></tr>
    <tr><td>建立「代結帳區」雲端共用表格</td><td>Mary ＋ 主任</td><td>8/1 前完成</td></tr>
    <tr><td>主任報到日確認（8/1 入職）</td><td>Jay</td><td>待確認</td></tr>
    <tr><td>主任入職後執行全倉盤點</td><td>主任</td><td>8/1 入職後第一週</td></tr>
    <tr><td>微信公司手機交接，更新微信顯示名稱</td><td>Mary ＋ 主任</td><td>8/1 入職時</td></tr>
    <tr><td>大陸倉售價與移倉清單交接給主任</td><td>Mary</td><td>8/1 入職時</td></tr>
    <tr><td>Ultra 已被取代庫存下架並執行下價</td><td>Mary</td><td>待辦</td></tr>
  </table>
</div>

</div><!-- end body -->

<div class="footer">
  <p>Dentstage 凹痕工廠 PDR Tools ｜ www.dentstagetools.com.tw</p>
  <p>紀錄整理：Myke AI ｜ 2026.06.22</p>
</div>

</div>
</body>
</html>"""

out = pathlib.Path(r'C:\Users\User\Downloads\Myke_Agent\Dentstage凹痕工廠相關事項\會議紀錄_20260622_embed.html')
out.write_text(HTML, encoding='utf-8')
print('done', len(HTML))
