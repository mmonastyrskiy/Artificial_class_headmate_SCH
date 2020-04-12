#ifndef LOGIN_H
#define LOGIN_H

#include <QDialog>
#include "choosemode.h"

QT_BEGIN_NAMESPACE
namespace Ui { class LogIn; }
QT_END_NAMESPACE

class LogIn : public QDialog
{
    Q_OBJECT

public:
    LogIn(QWidget *parent = nullptr);
    ~LogIn();

private slots:
    void on_buttonBox_accepted();

private:
    Ui::LogIn *ui;
    ChooseMode *cwindow;

};
#endif // LOGIN_H
