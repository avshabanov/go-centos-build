
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Summary: Greeter Service
Name: %_package
Version: %_version
Release: %_release
License: BSD
Group: Applications/Internet
SOURCE0 : %{name}-%{version}.tar.gz
URL: https://example.com

Requires: systemd

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

# in builddir
cp -a * %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_sysconfdir}/systemd/system/greeter.service

%post
systemctl enable greeter.service
systemctl restart greeter.service

%preun
systemctl stop greeter.service
systemctl disable greeter.service

%changelog
* Thu Mar 01 2018  Alex Shabanov <avshabanov@gmail.com> 1.0-1
- Initial Version
