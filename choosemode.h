#ifndef CHOOSEMODE_H
#define CHOOSEMODE_H

#include <QWidget>
#include "controls.h"
#include "deploydatamenu.h"
namespace Ui {
class ChooseMode;
}

class ChooseMode : public QWidget
{
    Q_OBJECT

public:
    explicit ChooseMode(QWidget *parent = nullptr);
    ~ChooseMode();

private slots:
    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

private:
    Ui::ChooseMode *ui;
    Controls *cont;
    DeployDataMenu *ddm;
};

#endif // CHOOSEMODE_H
