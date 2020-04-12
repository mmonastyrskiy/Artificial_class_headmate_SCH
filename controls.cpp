#include "controls.h"
#include "ui_controls.h"

Controls::Controls(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Controls)
{
    ui->setupUi(this);
}

Controls::~Controls()
{
    delete ui;
}

void Controls::on_Start_Butt_clicked()
{
    system("SysStart-w.bat");
}

void Controls::on_NewMem_Butt_clicked()
{
    system("AddNew-w.bat");
}

void Controls::on_Learn_Butt_clicked()
{
    system("Learn-w.bat");
}
