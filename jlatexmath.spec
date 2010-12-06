Summary:	An implementation of LaTeX math mode wrote in Java
Name:		jlatexmath
Version:	0.8.5
Release:	%mkrel 2
License:	GPLv2+
Group:		Development/Java
URL:		http://sourceforge.net/projects/jlatexmath
Source0:	http://downloads.sourceforge.net/project/jlatexmath/%{name}-src-%{version}.zip
BuildRequires:	ant >= 0:1.6
BuildRequires:	java-rpmbuild
BuildRequires:	jpackage-utils >= 0:1.6
Requires:	jpackage-utils
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
JLaTeXMath is an implementation of LaTeX math mode wrote in Java.

%prep
%setup -qn %{name}-src-%{version}

# remove all binary libs
find -type f -name "*.jar" -exec rm -rf {} \;

%build
export CLASSPATH=
export OPT_JAR_LIST=:
%ant -Dbuild.sysclasspath=only

%install
rm -rf %{buildroot}

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p dist/*.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd  %{buildroot}%{_javadir} 
    #create symlink
    ln -s %{name}-%{version}.jar %{name}.jar
popd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
