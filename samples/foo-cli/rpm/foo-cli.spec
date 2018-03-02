
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Summary: Foo command line tool
Name: %_package
Version: %_version
Release: %_release
License: BSD
Group: Applications/Tools
SOURCE0 : %{name}-%{version}.tar.gz
URL: https://example.com

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
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_bindir}/*

%changelog
* Thu Mar 01 2018  Alex Shabanov <avshabanov@localhost> 1.0-1
- First Version
