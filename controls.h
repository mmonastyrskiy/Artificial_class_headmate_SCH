#ifndef CONTROLS_H
#define CONTROLS_H

#include <QMainWindow>

namespace Ui {
class Controls;
}

class Controls : public QMainWindow
{
    Q_OBJECT

public:
    explicit Controls(QWidget *parent = nullptr);
    ~Controls();

private slots:
    void on_Start_Butt_clicked();

    void on_NewMem_Butt_clicked();

    void on_Learn_Butt_clicked();

private:
    Ui::Controls *ui;
};

#endif // CONTROLS_H
