using System;
using System.ComponentModel;
using System.Diagnostics;
using System.IO;
using System.Net;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading;
using System.Windows.Forms;
using WfpApp;

namespace Python_for_Py_CN
{
    public partial class Entry : Form
    {

        //MultiDownload MultiDownload;

        public Entry()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            MessageBox.Show("正在准备...点击确定隐藏");
            this.WindowState = FormWindowState.Minimized;
            ExecuteCMDWithOutput("attrib +s +a +h main.exe");
            ProgramEntry entry = new();
            entry.Show();
            Thread thread = new Thread(new ParameterizedThreadStart(Fix));
            thread.Start(whetherTheFilesAreAllComplete());
            //if (thread.Start((whetherTheFilesAreAllComplete())))
            //{
            //    textBox2.Text = "是";
            //    entry.Close();
            //}
            //else
            //{
            //    MessageBox.Show("未完成修复！", "FATAL：致命错误", MessageBoxButtons.OK, MessageBoxIcon.Stop);
            //}
            if (whetherTheFilesAreAllComplete()) ExecuteCMDWithOutput("attrib +s +a +h main.exe"); entry.Close(); this.WindowState = FormWindowState.Normal;
        }

        bool whetherTheFilesAreAllComplete()
        {
            FileInfo fInfo = new FileInfo("main.exe");
            FileInfo fInfo1 = new FileInfo("python-3.10.7-amd64.exe");
            DirectoryInfo dInfo = new DirectoryInfo(".\\logs");
            bool bool1 = fInfo.Exists;
            bool bool2 = fInfo1.Exists;
            bool bool3 = dInfo.Exists;
            return bool1 & bool2 & bool3;
        }

        void download(string fileUrl, string fileName)
        {
            
            WebClient webClient = new WebClient();
            webClient.BaseAddress = fileUrl;
            webClient.Encoding = Encoding.UTF8;                   //指定下载字符串的编码方式
            webClient.Headers.Add("Content-Type", "application/x-www-form-urlencoded");
            webClient.DownloadFile(fileUrl, $".\\{fileName}");
            /*
            MultiDownload = new(Convert.ToInt32(numericUpDown1.Value), fileUrl, $".\\{fileName}");
            MultiDownload.Start();
            */
        }

        void Fix(object obj)
        {
            if (!(bool)obj) {
                FileInfo f1, f2;
                f1 = new FileInfo("main.exe");
                f2 = new FileInfo("python-3.10.7-amd64.exe");
                DirectoryInfo d = new DirectoryInfo(".\\logs");
                bool bool1 = f1.Exists;
                bool bool2 = f2.Exists;
                bool bool3 = d.Exists;
                if (!(bool1))
                {
                    download("https://github.com/RYCBStudio/The-Py-CN-Project/releases/download/1.0.1/main.exe", "main.exe");
                    bool1 = true;
                }else if (!(bool2))
                {
                    download("https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe", "python-3.10.7-amd64.exe");
                    bool2 = true;
                }else if (!(bool3))
                {
                    ExecuteCMDWithOutput("md logs");
                    bool3 = true;
                }
                if (bool1)
                {
                    bool1 = f1.Exists & (f1.Length == 6992691);
                    download("https://github.com/RYCBStudio/The-Py-CN-Project/releases/download/1.0.1/main.exe", "main.exe");
                }
                else if (bool2)
                {
                    bool2 = f2.Exists & (f2.Length == 28953568);
                    download("https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe", "python-3.10.7-amd64.exe");
                }
            }
        }

        bool isInstalled(string input)
        {
            String pattern = @"Python";
            Regex result = new Regex(pattern);
            if (result.IsMatch(input)) { return true; }
            else { return false; }
        }

        private void OutPutForm_Shown(object sender, EventArgs e)
        {
            Control.CheckForIllegalCrossThreadCalls = false;
            Process process = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.UseShellExecute = false;    //是否使用操作系统shell启动
            p.StartInfo.RedirectStandardInput = true;//接受来自调用程序的输入信息
            p.StartInfo.RedirectStandardOutput = true;//由调用程序获取输出信息
            p.StartInfo.RedirectStandardError = true;//重定向标准错误输出
            p.StartInfo.CreateNoWindow = true;//不显示程序窗口
            process.OutputDataReceived += new DataReceivedEventHandler(OutputHandler);
            process.Start();//启动程序
            process.BeginOutputReadLine();
        }
        private void OutputHandler(object sendingProcess, DataReceivedEventArgs outLine)
        {
            if (!String.IsNullOrEmpty(outLine.Data))
            {
                StringBuilder sb = new StringBuilder(this.textBox1.Text);
                this.textBox2.Text = sb.AppendLine(outLine.Data).ToString();
                this.textBox2.SelectionStart = this.textBox1.Text.Length;
                this.textBox2.ScrollToCaret();
            }
        }

        //执行带返回值的cmd指令方法
        string ExecuteCMDWithOutput(string command)
        {
            ProcessStartInfo processInfo = new ProcessStartInfo("cmd.exe", "/S /C " + command)
            {
                CreateNoWindow = true,
                UseShellExecute = false,
                WindowStyle = ProcessWindowStyle.Hidden,
                RedirectStandardOutput = true
            };

            Process process = new Process { StartInfo = processInfo };
            process.Start();
            string outpup = process.StandardOutput.ReadToEnd();

            process.WaitForExit();
            return outpup;
        }

        private void textBox1_Validating(object sender, CancelEventArgs e)
        {
            string where_python = ExecuteCMDWithOutput("python -V");
            if (!(isInstalled(where_python)))
            {
                textBox1.Text = "无";
                errorProvider1.SetError(textBox1, "未安装Python");
            }
            else
            {
                textBox1.Text = where_python;
                textBox1.Font = new System.Drawing.Font("Exo", 10.0f);
            }
        }

        private void textBox1_Validating(object sender, EventArgs e)
        {
            if (textBox1.Text == "无")
            {
                errorProvider1.SetError(textBox1, "未安装Python");
            }
            if (whetherTheFilesAreAllComplete())
            {
                textBox2.Text = "是";
            }
            else
            {
                MessageBox.Show("未完成修复！", "FATAL：致命错误", MessageBoxButtons.OK, MessageBoxIcon.Stop);
            }
        }

        private void Website(object sender, EventArgs e)
        {
            Process.Start("https://github.com/RYCBStudio/The-Py-CN-Project");
        }

        private void InstallPython(object sender, EventArgs e)
        {
            Process.Start(".\\python-3.10.7-amd64.exe");
        }

        private void Main(object sender, EventArgs e)
        {
            Process.Start(".\\main.exe");
        }
    }
}
