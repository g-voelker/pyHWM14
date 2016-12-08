if __name__ == '__main__':

    def example01():

        from pyhwm2014.pyhwm14 import HWM14, HWM14Plot

        # Single Height profile    
        hwm14Obj = HWM14( altlim=[90,200], altstp=10, ap=[-1, 35], day=323,
            option=1, ut=11.66667, verbose=True, year=1993 )
            
        # Height profile plot
        hwm14Gbj = HWM14Plot( profObj=hwm14Obj )


    example01()