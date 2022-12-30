using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.Integration;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.Window;

namespace Python_for_Py_CN
{
    public partial class ProgramEntry : Form
    {
        int i, i1 = 0;

        Color[] colors = new Color[] { Color.Green, Color.FromArgb(0, 192, 0), Color.Lime, Color.FromArgb(128, 255, 128), Color.FromArgb(192, 255, 192), Color.FromArgb(128, 255, 128), Color.Lime, Color.FromArgb(0, 192, 0)};

        string[] texts = new string[] { "初始化", "初始化.", "初始化..", "初始化...", "初始化....", "初始化.....", "初始化......", "初始化.......", "初始化........", "初始化........."};

        public ProgramEntry()
        {
            InitializeComponent();
        }

        private void ProgramEntry_MouseDown(object sender, MouseEventArgs e)
        {
            ReleaseCapture();                        //用来释放被当前线程中某个窗口捕获的光标
            SendMessage(this.Handle, WM_SYSCOMMAND, SC_MOVE + HTCAPTION, 0);  //向Windows发送拖动窗体的消息
        }

        private void init(object sender, EventArgs e)
        {
            if (i >= colors.Length)
                i = 0;
            if (i1 >= texts.Length)
                i1 = 0;
            label2.ForeColor = colors[i];
            label2.Text = texts[i1];
            i++;
            i1++;
        }

        [DllImport("user32.dll")]
        public static extern bool ReleaseCapture();         //用来释放被当前线程中某个窗口捕获的光标

        [DllImport("user32.dll")]
        public static extern bool SendMessage(IntPtr hwdn, int wMsg, int mParam, int lParam);    //向指定的窗体发送Windows消息
        public const int WM_SYSCOMMAND = 0x0112;                     //该变量表示将向Windows发送的消息类型
        public const int SC_MOVE = 0xF010;                              //该变量表示发送消息的附加消息
        public const int HTCAPTION = 0x0002;                                 //该变量表示发送消息的附加消息
    }
}
