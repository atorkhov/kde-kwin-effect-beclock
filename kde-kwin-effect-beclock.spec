Name:           kde-kwin-effect-beclock
Version:        0.16
Release:        1%{?dist}
Summary:        A simple clock, implemented as KWin Effect

License:        GPLv2+
URL:            http://kde-look.org/content/show.php/BeClock?content=117542
Source0:        117542-beclock-kwin-fx-0.16.txz

BuildRequires:  cmake kdebase-workspace-devel libX11-devel mesa-libGL-devel mesa-libGLES-devel

%description
A simple clock, implemented as KWin Effect

- This is NO plasmoid!
- You need active desktop FX to use this clock
- The idea is somewhat experimental :-)


%prep
%setup -q -n beclock-kwin-fx-%{version}


%build
%{cmake_kde4}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%{_libdir}/kde4/kcm_kwin4_effect_beclock.so
%{_libdir}/kde4/kwin4_effect_beclock.so
%{_datadir}/kde4/services/kwin/beclock.desktop
%{_datadir}/kde4/services/kwin/beclock_config.desktop


%changelog
* Mon Jan 16 2012 Alexey Torkhov <atorkhov@gmail.com> - 0.16-1
- Initial package.

