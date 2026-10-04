import sys
import json
import ctypes
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from pynput import keyboard

GWL_EXSTYLE = -20
WS_EX_TRANSPARENT = 0x00000020

def resource_path(relative_path):
    """获取资源的绝对路径，兼容开发环境与 PyInstaller 打包后的环境"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

# ---------------------------------------------------------------------
# 多语言字典 (i18n) 
# ---------------------------------------------------------------------
LANG = {
    'zh': {
        'title': 'ZebraReader 导读条设置',
        'lbl_lang': '🌐 界面语言 (Language):',
        'lbl_opacity': '透 明 度 (Opacity):',
        'lbl_intensity': '色彩浓度 (Intensity):',
        'lbl_colors': '色彩循环序列 (按住拖拽可排序，双击修改):',
        'btn_add_color': '➕ 添加颜色',
        'btn_del_color': '➖ 删除选中',
        'lbl_templates': '💾 预设模板 (Templates):',
        'tpl_default': '🔒 默认经典模板 (不可更改)',
        'tpl_1': '自定义模板 1', 'tpl_2': '自定义模板 2', 'tpl_3': '自定义模板 3',
        'btn_load': '读取模板',
        'btn_save': '保存至选中模板',
        'btn_apply': '✔ 应用并隐藏面板',
        'tray_settings': '⚙️ 设置中心 (Settings)',
        'tray_donate': '☕ 请我喝杯咖啡 (Donate)',
        'tray_quit': '彻底退出',
        'donate_title': '赞赏开发者 / Buy me a coffee',
        'donate_cn_tab': '🇨🇳 中国大陆 (CN)',
        'donate_intl_tab': '🌍 国际 / Global',
        'donate_cn_msg': '<div style="font-size: 15px; color: #333; margin-bottom: 10px;"><b>感谢您的支持！☕</b></div>',
        'donate_intl_msg': (
            '<div style="font-size: 14px; color: #333; margin-bottom: 20px;">感谢您的支持！Thank you for your support!</div>'
            '<a href="https://ko-fi.com/felixliu339" style="text-decoration: none;">'
            '<span style="background-color: #29ABE0; color: white; padding: 10px 24px; font-weight: bold; font-size: 15px;">'
            ' ☕ Support me on Ko-fi '
            '</span></a><br><br><br>'
            '<div style="font-size: 13px; color: #666;">📱 <b>Nordic:</b> MobilePay Box (Code: <b>1872VC</b>)</div>'
        ),
        'help_title': 'ZebraReader 操作手册',
        'help_text': (
            "【快捷键 / Hotkeys】\n"
            "   • Ctrl + Y ： 显示 / Show\n"
            "   • Ctrl + Q ： 隐藏 / Hide\n"
            "   • Ctrl + Shift + H ： 显示此帮助 / Show Help\n\n"
            "【交互 / Mouse (When Visible)】\n"
            "   • 移动 / Move : Hold Ctrl + Drag\n"
            "   • 缩放 / Resize : Hold Ctrl + Alt + Drag edges\n"
            "   • 调行距 / Adjust : Hold Alt + Double Click\n"
            "     (拖拽虚线调整，再次 Alt+双击退出 / Drag lines, Double click to exit)"
        )
    },
    'en': {
        'title': 'ZebraReader Settings',
        'lbl_lang': '🌐 Language:',
        'lbl_opacity': 'Opacity:',
        'lbl_intensity': 'Color Intensity:',
        'lbl_colors': 'Color Sequence (Drag to reorder, Double click to edit):',
        'btn_add_color': '➕ Add Color',
        'btn_del_color': '➖ Remove Selected',
        'lbl_templates': '💾 Presets (Templates):',
        'tpl_default': '🔒 Default Classic (Locked)',
        'tpl_1': 'Custom Preset 1', 'tpl_2': 'Custom Preset 2', 'tpl_3': 'Custom Preset 3',
        'btn_load': 'Load Preset',
        'btn_save': 'Save to Selected',
        'btn_apply': '✔ Apply & Close',
        'tray_settings': '⚙️ Settings',
        'tray_donate': '☕ Buy me a coffee',
        'tray_quit': 'Quit Application',
        'donate_title': 'Support the Developer',
        'donate_cn_tab': '🇨🇳 China (WeChat/Alipay)',
        'donate_intl_tab': '🌍 Global',
        'donate_cn_msg': '<div style="font-size: 15px; color: #333; margin-bottom: 10px;"><b>Thanks for your support! ☕</b></div>',
        'donate_intl_msg': (
            '<div style="font-size: 15px; color: #333; margin-bottom: 20px;">Thank you for your support!</div>'
            '<a href="https://ko-fi.com/felixliu339" style="text-decoration: none;">'
            '<span style="background-color: #29ABE0; color: white; padding: 10px 24px; font-weight: bold; font-size: 15px;">'
            ' ☕ Support me on Ko-fi '
            '</span></a><br><br><br>'
            '<div style="font-size: 13px; color: #666;">📱 <b>Nordic:</b> MobilePay Box (Code: <b>1872VC</b>)</div>'
        ),
        'help_title': 'ZebraReader Manual',
        'help_text': (
            "【Hotkeys】\n"
            "   • Ctrl + Y : Show Overlay\n"
            "   • Ctrl + Q : Hide to Tray\n"
            "   • Ctrl + Shift + H : Show this Help\n\n"
            "【Mouse Interaction (When Visible)】\n"
            "   • Move : Hold Ctrl + Drag inside\n"
            "   • Resize : Hold Ctrl + Alt + Drag edges\n"
            "   • Adjust Line Height : Hold Alt + Double Click\n"
            "     (Drag dashed lines to adjust, Alt+Double Click again to exit)"
        )
    },
    'ja': {
        'title': 'ZebraReader 設定',
        'lbl_lang': '🌐 言語 (Language):',
        'lbl_opacity': '不透明度 (Opacity):',
        'lbl_intensity': '色の濃さ (Intensity):',
        'lbl_colors': 'カラーサイクル (ドラッグで並べ替え、ダブルクリックで編集):',
        'btn_add_color': '➕ 色を追加',
        'btn_del_color': '➖ 選択した色を削除',
        'lbl_templates': '💾 テンプレート (Templates):',
        'tpl_default': '🔒 デフォルト (変更不可)',
        'tpl_1': 'カスタムプリセット 1', 'tpl_2': 'カスタムプリセット 2', 'tpl_3': 'カスタムプリセット 3',
        'btn_load': '読み込む',
        'btn_save': '選択した項目に保存',
        'btn_apply': '✔ 適用して閉じる',
        'tray_settings': '⚙️ 設定 (Settings)',
        'tray_donate': '☕ コーヒーを奢る (Donate)',
        'tray_quit': '終了 (Quit)',
        'donate_title': '開発者を支援 / Buy me a coffee',
        'donate_cn_tab': '🇨🇳 中国 (Alipay/WeChat)',
        'donate_intl_tab': '🌍 グローバル / Global',
        'donate_cn_msg': '<div style="font-size: 15px; color: #333; margin-bottom: 10px;"><b>ご支援ありがとうございます！☕</b></div>',
        'donate_intl_msg': (
            '<div style="font-size: 14px; color: #333; margin-bottom: 20px;">ご支援ありがとうございます！Thank you for your support!</div>'
            '<a href="https://ko-fi.com/felixliu339" style="text-decoration: none;">'
            '<span style="background-color: #29ABE0; color: white; padding: 10px 24px; font-weight: bold; font-size: 15px;">'
            ' ☕ Support me on Ko-fi '
            '</span></a><br><br><br>'
            '<div style="font-size: 13px; color: #666;">📱 <b>Nordic:</b> MobilePay Box (Code: <b>1872VC</b>)</div>'
        ),
        'help_title': 'ZebraReader マニュアル',
        'help_text': (
            "【ショートカット / Hotkeys】\n"
            "   • Ctrl + Y ： 表示する\n"
            "   • Ctrl + Q ： 隠す\n"
            "   • Ctrl + Shift + H ： このヘルプを表示\n\n"
            "【マウス操作 (表示中)】\n"
            "   • 移動 : Ctrl を押しながらドラッグ\n"
            "   • サイズ変更 : Ctrl + Alt を押しながら端をドラッグ\n"
            "   • 行の高さ調整 : Alt + ダブルクリック\n"
            "     (点線をドラッグして調整、再度 Alt+ダブルクリックで終了)"
        )
    }
}

DEFAULT_CONFIG = {
    'colors': ["#a5e696", "#ffa0b4", "#8cdcf0", "#fff578"],
    'opacity': 0.30,
    'intensity': 1.0,
    'line_height': 42
}

# ---------------------------------------------------------------------
# 全局键盘监听器
# ---------------------------------------------------------------------
class GlobalKeyListener(QtCore.QThread):
    mods_changed = QtCore.pyqtSignal(bool, bool)
    hotkey_show = QtCore.pyqtSignal()
    hotkey_hide = QtCore.pyqtSignal()
    hotkey_help = QtCore.pyqtSignal()

    def run(self):
        self.ctrl = self.alt = self.shift = False
        VK_Y, VK_Q, VK_H = 0x59, 0x51, 0x48

        def on_press(key):
            if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.ctrl):
                self.ctrl = True
                self.mods_changed.emit(self.ctrl, self.alt)
            elif key in (keyboard.Key.alt_l, keyboard.Key.alt_r, keyboard.Key.alt):
                self.alt = True
                self.mods_changed.emit(self.ctrl, self.alt)
            elif key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
                self.shift = True

            if hasattr(key, 'vk') and key.vk is not None:
                if key.vk == VK_Y and self.ctrl and not self.shift and not self.alt:
                    self.hotkey_show.emit()
                elif key.vk == VK_Q and self.ctrl and not self.shift and not self.alt:
                    self.hotkey_hide.emit()
                elif key.vk == VK_H and self.ctrl and self.shift and not self.alt:
                    self.hotkey_help.emit()

        def on_release(key):
            if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r, keyboard.Key.ctrl):
                self.ctrl = False
                self.mods_changed.emit(self.ctrl, self.alt)
            elif key in (keyboard.Key.alt_l, keyboard.Key.alt_r, keyboard.Key.alt):
                self.alt = False
                self.mods_changed.emit(self.ctrl, self.alt)
            elif key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
                self.shift = False

        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

# ---------------------------------------------------------------------
# 设置界面
# ---------------------------------------------------------------------
class SettingsWindow(QtWidgets.QDialog):
    config_applied = QtCore.pyqtSignal(dict)
    
    def __init__(self, settings_db, parent=None):
        super().__init__(parent)
        self.db = settings_db
        self.current_lang = self.db.value("lang", "zh")
        if self.current_lang not in LANG:
            self.current_lang = 'zh'
            
        self.init_ui()
        self.load_template(0)
        
    def tr(self, key):
        return LANG[self.current_lang].get(key, key)
        
    def init_ui(self):
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle(self.tr('title'))
        self.resize(380, 500)
        
        icon_path = resource_path("icon_zebra.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QtGui.QIcon(icon_path))
            
        layout = QtWidgets.QVBoxLayout(self)

        lang_layout = QtWidgets.QHBoxLayout()
        self.lbl_lang = QtWidgets.QLabel(self.tr('lbl_lang'))
        self.cb_lang = QtWidgets.QComboBox()
        self.cb_lang.addItems(["中文", "English", "日本語"])
        
        if self.current_lang == 'zh': self.cb_lang.setCurrentIndex(0)
        elif self.current_lang == 'en': self.cb_lang.setCurrentIndex(1)
        elif self.current_lang == 'ja': self.cb_lang.setCurrentIndex(2)
            
        self.cb_lang.currentIndexChanged.connect(self.change_lang)
        lang_layout.addWidget(self.lbl_lang)
        lang_layout.addWidget(self.cb_lang)
        layout.addLayout(lang_layout)
        layout.addWidget(QtWidgets.QFrame(frameShape=QtWidgets.QFrame.HLine))

        self.lbl_op = QtWidgets.QLabel(self.tr('lbl_opacity'))
        self.sld_op = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sld_op.setRange(5, 80)
        layout.addWidget(self.lbl_op)
        layout.addWidget(self.sld_op)

        self.lbl_int = QtWidgets.QLabel(self.tr('lbl_intensity'))
        self.sld_int = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sld_int.setRange(20, 200) 
        layout.addWidget(self.lbl_int)
        layout.addWidget(self.sld_int)

        self.lbl_col = QtWidgets.QLabel(self.tr('lbl_colors'))
        layout.addWidget(self.lbl_col)
        
        self.color_list = QtWidgets.QListWidget()
        self.color_list.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.color_list.itemDoubleClicked.connect(self.edit_color)
        layout.addWidget(self.color_list)

        btn_layout = QtWidgets.QHBoxLayout()
        self.btn_add_c = QtWidgets.QPushButton(self.tr('btn_add_color'))
        self.btn_add_c.clicked.connect(lambda: self.add_color())
        self.btn_del_c = QtWidgets.QPushButton(self.tr('btn_del_color'))
        self.btn_del_c.clicked.connect(self.del_color)
        btn_layout.addWidget(self.btn_add_c)
        btn_layout.addWidget(self.btn_del_c)
        layout.addLayout(btn_layout)
        
        layout.addWidget(QtWidgets.QFrame(frameShape=QtWidgets.QFrame.HLine))

        self.lbl_tpl = QtWidgets.QLabel(self.tr('lbl_templates'))
        layout.addWidget(self.lbl_tpl)
        self.cb_tpl = QtWidgets.QComboBox()
        self.update_template_names()
        
        tpl_btn_layout = QtWidgets.QHBoxLayout()
        self.btn_load = QtWidgets.QPushButton(self.tr('btn_load'))
        self.btn_load.clicked.connect(lambda: self.load_template(self.cb_tpl.currentIndex()))
        self.btn_save = QtWidgets.QPushButton(self.tr('btn_save'))
        self.btn_save.clicked.connect(self.save_template)
        tpl_btn_layout.addWidget(self.cb_tpl)
        tpl_btn_layout.addWidget(self.btn_load)
        tpl_btn_layout.addWidget(self.btn_save)
        layout.addLayout(tpl_btn_layout)

        self.btn_apply = QtWidgets.QPushButton(self.tr('btn_apply'))
        self.btn_apply.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; padding: 10px;")
        self.btn_apply.clicked.connect(self.apply_config)
        layout.addWidget(self.btn_apply)

    def update_template_names(self):
        self.cb_tpl.clear()
        self.cb_tpl.addItems([self.tr('tpl_default'), self.tr('tpl_1'), self.tr('tpl_2'), self.tr('tpl_3')])

    def change_lang(self):
        idx = self.cb_lang.currentIndex()
        if idx == 0: self.current_lang = 'zh'
        elif idx == 1: self.current_lang = 'en'
        elif idx == 2: self.current_lang = 'ja'
            
        self.db.setValue("lang", self.current_lang)
        self.setWindowTitle(self.tr('title'))
        self.lbl_lang.setText(self.tr('lbl_lang'))
        self.lbl_op.setText(self.tr('lbl_opacity'))
        self.lbl_int.setText(self.tr('lbl_intensity'))
        self.lbl_col.setText(self.tr('lbl_colors'))
        self.btn_add_c.setText(self.tr('btn_add_color'))
        self.btn_del_c.setText(self.tr('btn_del_color'))
        self.lbl_tpl.setText(self.tr('lbl_templates'))
        self.btn_load.setText(self.tr('btn_load'))
        self.btn_save.setText(self.tr('btn_save'))
        self.btn_apply.setText(self.tr('btn_apply'))
        
        cb_idx = self.cb_tpl.currentIndex()
        self.update_template_names()
        self.cb_tpl.setCurrentIndex(cb_idx)
        self.config_applied.emit(self.get_current_config())

    def add_color(self, hex_val="#ffffff"):
        item = QtWidgets.QListWidgetItem(hex_val)
        item.setBackground(QtGui.QColor(hex_val))
        self.color_list.addItem(item)

    def del_color(self):
        if self.color_list.currentRow() >= 0:
            self.color_list.takeItem(self.color_list.currentRow())

    def edit_color(self, item):
        color = QtWidgets.QColorDialog.getColor(item.background().color(), self)
        if color.isValid():
            item.setBackground(color)
            item.setText(color.name())

    def load_template(self, index):
        if index == 0:
            config = DEFAULT_CONFIG
        else:
            saved = self.db.value(f"tpl_{index}")
            config = json.loads(saved) if saved else DEFAULT_CONFIG
        
        self.sld_op.setValue(int(config['opacity'] * 100))
        self.sld_int.setValue(int(config['intensity'] * 100))
        self.color_list.clear()
        for c in config['colors']:
            self.add_color(c)

    def save_template(self):
        idx = self.cb_tpl.currentIndex()
        if idx == 0:
            QtWidgets.QMessageBox.warning(self, "Warning", "Default template is locked!")
            return
        self.db.setValue(f"tpl_{idx}", json.dumps(self.get_current_config()))

    def get_current_config(self):
        colors = [self.color_list.item(i).text() for i in range(self.color_list.count())]
        return {
            'colors': colors if colors else ["#ffffff"],
            'opacity': self.sld_op.value() / 100.0,
            'intensity': self.sld_int.value() / 100.0,
            'line_height': 42 
        }

    def apply_config(self):
        self.config_applied.emit(self.get_current_config())
        self.hide()


# ---------------------------------------------------------------------
# 主覆盖层逻辑
# ---------------------------------------------------------------------
class GlassReadingStrip(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.db = QtCore.QSettings("FelixDev", "ZebraReader")
        
        self.line_height = 42
        self.opacity = 0.30
        self.intensity = 1.0
        self.colors = []
        self.is_ctrl = self.is_alt = self.line_edit_mode = False
        self.is_passthrough = True
        self.drag_mode = None

        self.init_window()
        self.settings_window = SettingsWindow(self.db)
        self.settings_window.config_applied.connect(self.update_from_settings)
        
        self.init_tray()
        self.start_keyboard_listener()
        
        self.settings_window.apply_config()
        self.settings_window.show()

    def tr(self, key):
        return LANG[self.settings_window.current_lang].get(key, key)

    def update_from_settings(self, config):
        self.opacity = config['opacity']
        self.intensity = config['intensity']
        self.colors = [QtGui.QColor(c) for c in config['colors']]
        self.update_tray_menu()
        self.update()

    def init_window(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setMouseTracking(True)
        self.resize(700, 900)
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        self.move((screen.width() - self.width()) // 2, (screen.height() - self.height()) // 2)
        self.show()
        self.update_passthrough_state()

    def init_tray(self):
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.update_tray_icon()
        self.tray_icon.activated.connect(self.on_tray_activated)
        self.tray_icon.show()
        self.update_tray_menu()

    def update_tray_icon(self):
        icon_path = resource_path("icon_z.png")
        if os.path.exists(icon_path):
            self.tray_icon.setIcon(QtGui.QIcon(icon_path))
        else:
            pixmap = QtGui.QPixmap(32, 32)
            pixmap.fill(QtCore.Qt.transparent)
            p = QtGui.QPainter(pixmap)
            draw_colors = self.colors if self.colors else [QtGui.QColor("#ccc")]
            h_step = 32 / len(draw_colors)
            for i, c in enumerate(draw_colors):
                p.fillRect(0, int(i * h_step), 32, int(h_step) + 1, c)
            p.end()
            self.tray_icon.setIcon(QtGui.QIcon(pixmap))

    def update_tray_menu(self):
        self.tray_icon.setToolTip("ZebraReader")
        menu = QtWidgets.QMenu()
        menu.addAction(self.tr('tray_settings')).triggered.connect(self.settings_window.show)
        menu.addAction(self.tr('tray_donate')).triggered.connect(self.show_donate)
        menu.addSeparator()
        menu.addAction("📖 Ctrl+Shift+H").triggered.connect(self.show_help_manual)
        menu.addSeparator()
        menu.addAction(self.tr('tray_quit')).triggered.connect(QtWidgets.qApp.quit)
        self.tray_icon.setContextMenu(menu)

    def show_donate(self):
        msg = QtWidgets.QDialog()
        msg.setWindowTitle(self.tr('donate_title'))
        msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        msg.resize(360, 480)
        
        msg.setStyleSheet("""
            QDialog { 
                background-color: #F8F9FA; 
            }
            QTabWidget::pane { 
                border: 1px solid #E0E0E0; 
                background-color: #FFFFFF;
                border-radius: 6px;
            }
            QTabBar::tab { 
                background: #E9ECEF; 
                color: #555555;
                padding: 10px 20px; 
                margin-right: 2px;
                border-top-left-radius: 6px; 
                border-top-right-radius: 6px;
                font-size: 13px;
                font-weight: bold;
            }
            QTabBar::tab:selected { 
                background: #FFFFFF; 
                color: #2196F3;
                border: 1px solid #E0E0E0;
                border-bottom: none;
            }
        """)
        
        layout = QtWidgets.QVBoxLayout(msg)
        layout.setContentsMargins(15, 15, 15, 15)
        
        tabs = QtWidgets.QTabWidget()
        
        tab_cn = QtWidgets.QWidget()
        lay_cn = QtWidgets.QVBoxLayout(tab_cn)
        lay_cn.setContentsMargins(20, 30, 20, 20)
        lay_cn.setSpacing(15)
        
        lbl_cn = QtWidgets.QLabel(self.tr('donate_cn_msg'))
        lbl_cn.setAlignment(QtCore.Qt.AlignCenter)
        lay_cn.addWidget(lbl_cn)
        
        qr_path = resource_path("Alipay.png")
        if os.path.exists(qr_path):
            lbl_img = QtWidgets.QLabel()
            lbl_img.setStyleSheet("border: 1px solid #EAEAEA; padding: 10px; border-radius: 8px; background: white;")
            lbl_img.setPixmap(QtGui.QPixmap(qr_path).scaled(230, 230, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            lbl_img.setAlignment(QtCore.Qt.AlignCenter)
            lay_cn.addWidget(lbl_img)
        lay_cn.addStretch()
        tabs.addTab(tab_cn, self.tr('donate_cn_tab'))
        
        tab_intl = QtWidgets.QWidget()
        lay_intl = QtWidgets.QVBoxLayout(tab_intl)
        lay_intl.setContentsMargins(20, 30, 20, 20)
        lay_intl.setSpacing(15)
        
        lbl_intl = QtWidgets.QLabel(self.tr('donate_intl_msg'))
        lbl_intl.setAlignment(QtCore.Qt.AlignCenter)
        lbl_intl.setOpenExternalLinks(True) 
        lay_intl.addWidget(lbl_intl)
        
        mp_qr_path = resource_path("mobilepay QR.jpeg")
        if os.path.exists(mp_qr_path):
            lbl_mp = QtWidgets.QLabel()
            lbl_mp.setStyleSheet("border: 1px solid #EAEAEA; padding: 10px; border-radius: 8px; background: white;")
            lbl_mp.setPixmap(QtGui.QPixmap(mp_qr_path).scaled(230, 230, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
            lbl_mp.setAlignment(QtCore.Qt.AlignCenter)
            lay_intl.addWidget(lbl_mp)
            
        lay_intl.addStretch()
        tabs.addTab(tab_intl, self.tr('donate_intl_tab'))

        layout.addWidget(tabs)
        msg.exec_()

    def show_help_manual(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(self.tr('help_title'))
        msg.setText(self.tr('help_text'))
        msg.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        msg.exec_()

    def on_tray_activated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.settings_window.show()

    def show_overlay(self):
        self.show()
        self.raise_()
        self.update_passthrough_state()

    def hide_overlay(self):
        self.hide()

    def start_keyboard_listener(self):
        self.listener = GlobalKeyListener()
        self.listener.mods_changed.connect(self.on_modifiers_changed)
        self.listener.hotkey_show.connect(self.show_overlay)
        self.listener.hotkey_hide.connect(self.hide_overlay)
        self.listener.hotkey_help.connect(self.show_help_manual)
        self.listener.start()

    @QtCore.pyqtSlot(bool, bool)
    def on_modifiers_changed(self, ctrl, alt):
        self.is_ctrl = ctrl
        self.is_alt = alt
        if self.isVisible():
            self.update_passthrough_state()
            self.update()

    def update_passthrough_state(self):
        hwnd = int(self.winId())
        user32 = ctypes.windll.user32
        ex_style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)

        needs_interaction = self.is_ctrl or self.is_alt or self.line_edit_mode
        should_passthrough = not needs_interaction

        if should_passthrough != self.is_passthrough:
            self.is_passthrough = should_passthrough
            if should_passthrough:
                user32.SetWindowLongW(hwnd, GWL_EXSTYLE, ex_style | WS_EX_TRANSPARENT)
            else:
                user32.SetWindowLongW(hwnd, GWL_EXSTYLE, ex_style & ~WS_EX_TRANSPARENT)

    def adjust_color_intensity(self, color):
        h, s, l, a = color.getHslF()
        new_s = max(0.0, min(1.0, s * self.intensity))
        return QtGui.QColor.fromHslF(h, new_s, l, a)

    def paintEvent(self, event):
        if not self.colors: return
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing, False)
        w, h = self.width(), self.height()
        y, idx = 0, 0
        color_count = len(self.colors)
        
        while y < h:
            base_c = self.colors[idx % color_count]
            draw_c = self.adjust_color_intensity(base_c)
            draw_c.setAlphaF(self.opacity)
            painter.fillRect(0, int(y), w, int(self.line_height), draw_c)

            if self.line_edit_mode:
                pen = QtGui.QPen(QtGui.QColor(0, 0, 0, 100), 2, QtCore.Qt.DashLine)
                painter.setPen(pen)
                painter.drawLine(0, int(y + self.line_height), w, int(y + self.line_height))

            y += self.line_height
            idx += 1

        if (self.is_ctrl and self.is_alt) or self.drag_mode == 'resize':
            pen = QtGui.QPen(QtGui.QColor(140, 140, 140, 220), 3)
            painter.setPen(pen)
            painter.drawRect(1, 1, w - 2, h - 2)

    def mouseDoubleClickEvent(self, event):
        if self.is_alt and event.button() == QtCore.Qt.LeftButton:
            self.line_edit_mode = not self.line_edit_mode
            self.update_passthrough_state()
            self.update()

    def mousePressEvent(self, event):
        if event.button() != QtCore.Qt.LeftButton: return
        self.drag_start_pos = event.globalPos()
        self.drag_start_geometry = self.geometry()

        if self.line_edit_mode:
            y = event.y()
            index = round(y / self.line_height)
            if index > 0 and abs(y - index * self.line_height) < 15:
                self.drag_mode = 'resize_line'
                self.drag_line_index = index
                return

        if self.is_ctrl and self.is_alt:
            margin = 15
            x, y = event.x(), event.y()
            w, h = self.width(), self.height()
            self.drag_edges = []
            if x < margin: self.drag_edges.append('left')
            elif x > w - margin: self.drag_edges.append('right')
            if y < margin: self.drag_edges.append('top')
            elif y > h - margin: self.drag_edges.append('bottom')
            self.drag_mode = 'resize' if self.drag_edges else 'move'
            return

        if self.is_ctrl and not self.is_alt:
            self.drag_mode = 'move'

    def mouseMoveEvent(self, event):
        if not event.buttons():
            if self.line_edit_mode:
                y = event.y()
                index = round(y / self.line_height)
                if index > 0 and abs(y - index * self.line_height) < 15:
                    self.setCursor(QtCore.Qt.SizeVerCursor)
                else:
                    self.setCursor(QtCore.Qt.ArrowCursor)
            elif self.is_ctrl and self.is_alt:
                margin = 15
                x, y = event.x(), event.y()
                w, h = self.width(), self.height()
                e_l, e_r, e_t, e_b = x < margin, x > w - margin, y < margin, y > h - margin
                if (e_l and e_t) or (e_r and e_b): self.setCursor(QtCore.Qt.SizeFDiagCursor)
                elif (e_l and e_b) or (e_r and e_t): self.setCursor(QtCore.Qt.SizeBDiagCursor)
                elif e_l or e_r: self.setCursor(QtCore.Qt.SizeHorCursor)
                elif e_t or e_b: self.setCursor(QtCore.Qt.SizeVerCursor)
                else: self.setCursor(QtCore.Qt.SizeAllCursor)
            else:
                self.setCursor(QtCore.Qt.ArrowCursor)
            return

        if not self.drag_mode: return
        delta = event.globalPos() - self.drag_start_pos
        if self.drag_mode == 'move':
            self.move(self.drag_start_geometry.topLeft() + delta)
        elif self.drag_mode == 'resize':
            rect = QtCore.QRect(self.drag_start_geometry)
            if 'left' in self.drag_edges: rect.setLeft(rect.left() + delta.x())
            if 'right' in self.drag_edges: rect.setRight(rect.right() + delta.x())
            if 'top' in self.drag_edges: rect.setTop(rect.top() + delta.y())
            if 'bottom' in self.drag_edges: rect.setBottom(rect.bottom() + delta.y())
            self.setGeometry(rect)
        elif self.drag_mode == 'resize_line':
            new_y = event.y()
            if new_y > 15:
                self.line_height = new_y / self.drag_line_index
                self.update()

    def mouseReleaseEvent(self, event):
        self.drag_mode = None
        self.setCursor(QtCore.Qt.ArrowCursor)

if __name__ == '__main__':
    QtWidgets.QApplication.setQuitOnLastWindowClosed(False)
    app = QtWidgets.QApplication(sys.argv)
    overlay = GlassReadingStrip()
    sys.exit(app.exec_())

